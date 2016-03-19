# Twitter Users Statistics

Configuration
---

1. Go to https://apps.twitter.com/, create a new application.
2. Go to 'Keys and Access Tokens' tab, press on 'Generate Access Token'
3. Start tus.py, it will create an empty config.json file
4. Edit config.json and put all the request data in the empty fields.
5. The tracked accounts are listed in "accounts" as list of twitter usernames


Start
---

```python
	python3 tus.py
```

This will produce:

data/followers.csv
data/following.csv

where:

time,account1,account2,account3,...
timestamp,n1,n2,n3,...

