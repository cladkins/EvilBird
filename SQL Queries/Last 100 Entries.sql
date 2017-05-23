SELECT * FROM (SELECT * FROM twitter ORDER BY created_at DESC LIMIT 100)sub ORDER BY created_at DESC;
