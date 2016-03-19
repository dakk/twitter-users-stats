import datetime
import time
import requests
import json
import sys
import os

conf = { "accounts": ["dagide"], "destination": "data/"}

def getUser (account):
	r = requests.get ('http://twitter.com/' + account)
	followers = r.text.split ('ProfileNav-value')[1].split ('>')[1].split ('<')[0]
	following = r.text.split ('ProfileNav-value')[2].split ('>')[1].split ('<')[0]
	return (followers, following)

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


if True:
	fwers = open (conf['destination'] + 'followers.csv', 'a')
	fwing = open (conf['destination'] + 'following.csv', 'a')

	t = datetime.datetime.now().ctime ()
	fwers.write (t)
	fwing.write (t)

	for acc in conf['accounts']:
		print ('Inspecting %s' % acc)
		try:
			p = getUser (acc)
			fwers.write (',' + str (p[0]))
			fwing.write (',' + str (p[1]))
		except:
			fwers.write (',')
			fwing.write (',')

	fwers.write ('\n')
	fwing.write ('\n')		

	fwers.close ()
	fwing.close ()	

