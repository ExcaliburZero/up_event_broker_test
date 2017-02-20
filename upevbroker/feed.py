import requests

import sys
import time

import urllib
import urllib2

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

for line in lines:
    print line
    split = line.split(" ")
    times = float(split[0])
    light = float(split[1])
    errors = float(split[2])

    url = "http://localhost:5000/post"
    values = {
        'id': "OGLE 00002",
        'time': times,
        'magnitude': light,
        'error': errors
    }
    #data = urllib.urlencode(values)
    #data = str(values)
    data = values
    headers = {'Content-Type': 'application/json'}
    #req = urllib2.Request(url, data, headers)
    #response = urllib2.urlopen(req)
    r = requests.post("http://localhost:5000/post", json=data, headers=headers)

    print(r.status_code, r.reason)
    print(r.text)
    time.sleep(0.1)
