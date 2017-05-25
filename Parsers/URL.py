#!/usr/bin/env python
# This script is intended to run a MySql Query , return the resluts and then tweet them out

import MySQLdb
import requests
import tweepy


CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET=""

HOST=""
USER=""
PASSWD=""
DATABASE=""


auth=tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# open a database connection
cnx=MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DATABASE)

# Create DB connection Cursor
cursor=cnx.cursor()

# Create the MySql Query
query=(
	"SELECT * FROM tweets.twitter WHERE text regexp '^(https?://|www\\.)[\.A-Za-z0-9\-]+\\.[a-zA-Z]{2,4}' ORDER BY created_at DESC LIMIT 1;")

# Execution of the SELECT statement
cursor.execute(query, ())

# for (id, tweet_id, screen_name, created_at, text) in cursor:
# print(id, tweet_id, screen_name, created_at, text)

for (id, tweet_id, screen_name, created_at, text) in cursor:
	url='https://www.threatminer.org/domain.php'
	payload={'q': text, 'api': 'True', 'rt': '6'}
	headers={
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
	r=requests.get(url, params=payload, headers=headers)
	json_data=r.json()
	status_message=json_data['status_message']
	state_URL = 'URL'
	tweet_text = text
	tweet_message= 'was mentioned by'
	tweet_mention = '@'
	tweet_username = screen_name
	threatminer_url=url
	threatminer_param = '?q='
	tweet_url  = "{}{}{}".format(threatminer_url,threatminer_param, tweet_text)
	final_tweet = "{} {} {} {}{} {}".format(state_URL, tweet_text, tweet_message, tweet_mention, tweet_username, tweet_url)
	if "Results found." in status_message:
		api=tweepy.API(auth)
		api.update_status(final_tweet)
		print(final_tweet)
	else:
		print('Nothing')
		print(final_tweet)