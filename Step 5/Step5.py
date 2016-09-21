import httplib
import json
from datetime import timedelta
import dateutil.parser


params = json.dumps({'token': '97826876ae83ebe88b01cb310a430c91'}, separators=(',', ':'))
headers = {"Content-type": "application/json",
           "Accept": "text/plain"}
conn = httplib.HTTPConnection("challenge.code2040.org")
conn.request("POST", "/api/dating", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()

pythonDict = json.loads(data)

def addTime(pythonDict):
    stamp = pythonDict.get('datestamp')
    interval = pythonDict.get('interval')
    interval = timedelta(seconds=interval)
    datestamp = dateutil.parser.parse(stamp)
    datestamp= datestamp + interval
    datestamp = datestamp.replace(tzinfo=None)
    finalDate = datestamp.isoformat() + 'Z'
    return finalDate

date = addTime(pythonDict)

params = json.dumps({'token': '97826876ae83ebe88b01cb310a430c91', 'datestamp': date}, separators=(',',':'))
headers = {"Content-type": "application/json",
           "Accept": "text/plain"}
conn = httplib.HTTPConnection("challenge.code2040.org")
conn.request("POST", "/api/dating/validate", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()