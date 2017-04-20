import datetime
import time
import requests
import json
import sys
import os

conf = { "accounts": ["dagide"], "destination": "data/"}

def formatNumber (data):
	return data.replace (' ', '').replace ('\xa0', '').replace ('M', '000000').replace ('m', '000000').replace ('K', '000').replace ('k', '000').replace ('.', '').replace (',', '')

def getUser (account):
	r = requests.get ('http://twitter.com/' + account)
	tweets = formatNumber (r.text.split ('ProfileNav-value')[1].split ('>')[1].split ('<')[0])
	following = formatNumber (r.text.split ('ProfileNav-value')[2].split ('>')[1].split ('<')[0])
	followers = formatNumber (r.text.split ('ProfileNav-value')[3].split ('>')[1].split ('<')[0])
	return (tweets, followers, following)

try:
    with open ('config.json', 'r') as f:
        conf = json.loads (f.read ())
except:
    with open ('config.json', 'w') as f:
        f.write (json.dumps (conf, sort_keys=True, indent=4, separators=(',', ': ')))
        f.close ()
        print ('config.json created; restart the software after editing it')
        sys.exit (0)

try:
	os.mkdir (conf['destination'])
except:
	pass


try:
	fwers = open (conf['destination'] + 'followers.csv', 'r')
	d = fwers.readline ().replace ('\n', '')
	conf['accounts'] = d.split (',')[1:]
except:
	fwers = open (conf['destination'] + 'followers.csv', 'w')

	fwers.write ('time')
	for acc in conf['accounts']:
		fwers.write (',' + acc)
	fwers.write ('\n')
	fwers.close ()

try:
	fwing = open (conf['destination'] + 'following.csv', 'r')
	d = fwing.readline ().replace ('\n', '')
	conf['accounts'] = d.split (',')[1:]
except:
	fwing = open (conf['destination'] + 'following.csv', 'w')

	fwing.write ('time')
	for acc in conf['accounts']:
		fwing.write (',' + acc)
	fwing.write ('\n')
	fwing.close ()


try:
	ftw = open (conf['destination'] + 'tweets.csv', 'r')
	d = ftw.readline ().replace ('\n', '')
	conf['accounts'] = d.split (',')[1:]
except:
	ftw = open (conf['destination'] + 'tweets.csv', 'w')

	ftw.write ('time')
	for acc in conf['accounts']:
		ftw.write (',' + acc)
	ftw.write ('\n')
	ftw.close ()


if True:
	fwers = open (conf['destination'] + 'followers.csv', 'a')
	fwing = open (conf['destination'] + 'following.csv', 'a')
	ftw = open (conf['destination'] + 'tweets.csv', 'a')

	t = datetime.datetime.now().ctime ()
	fwers.write (t)
	fwing.write (t)
	ftw.write (t)

	for acc in conf['accounts']:
		try:
			p = getUser (acc)
			print ('Inspecting %s' % acc, p)
			fwers.write (',' + str (p[1]))
			ftw.write (',' + str (p[0]))
			fwing.write (',' + str (p[2]))
		except:
			ftw.write (',')
			fwers.write (',')
			fwing.write (',')

	ftw.write ('\n')
	fwers.write ('\n')
	fwing.write ('\n')		

	ftw.close ()
	fwers.close ()
	fwing.close ()	

