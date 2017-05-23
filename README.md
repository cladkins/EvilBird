# Evil_Bird

This is the code behind the Twitter account `@_EvilBird_` 

**WHY**

Welcome to EvilBird, the goal of this project is to parse the Streaming tweets function of Twitter for malicious content.

**How**

This is accomplished by using the sample stream from Twitter and then placing it into a MySQL database. From there the information is parsed using REGEX and if a malicious item is found it will tweet the content along with the source used to determine the maliciousness. I am checking against ThreatMiner to see if it has been associated with any reports.

**What we are currently looking for:**

IP Addresses

MD5 Hashes


**Items I have utilized:**

http://pythondata.com/collecting-storing-tweets-python-mysql/
https://www.threatminer.org/about.php