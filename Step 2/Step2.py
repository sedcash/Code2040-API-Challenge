import httplib
import json

params = json.dumps({'token': '97826876ae83ebe88b01cb310a430c91'}, separators=(',', ':'))
headers = {"Content-type": "application/json",
           "Accept": "text/plain"}
conn = httplib.HTTPConnection("challenge.code2040.org")
conn.request("POST", "/api/reverse", params, headers)
response = conn.getresponse()
print response.status, response.reason
stringToReverse = response.read()
print stringToReverse
conn.close()

reverseString = stringToReverse[::-1]
print reverseString

params = json.dumps({'token': '97826876ae83ebe88b01cb310a430c91', 'string': reverseString}, separators=(',', ':'))
headers = {"Content-type": "application/json",
           "Accept": "text/plain"}
conn = httplib.HTTPConnection("challenge.code2040.org")
conn.request("POST", "/api/reverse/validate", params, headers)
print params
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()
