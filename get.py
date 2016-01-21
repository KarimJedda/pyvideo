import requests
import pprint
import time
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['pyvideo']
collection = db['videos']

base_link = 'http://pyvideo.org/api/v2/video/{}'
dont_be_a_jerk = 1

for i in xrange(5000):
	r = requests.get(base_link.format(i))	
	if not r.status_code == 200:
		print "Skipped entry {}".format(i)
		continue
	print "Added entry {}".format(i)
	collection.insert_one(r.json())
	time.sleep(dont_be_a_jerk)
	
