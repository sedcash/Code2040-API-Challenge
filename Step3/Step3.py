import httplib
import json

params = json.dumps({'token': '97826876ae83ebe88b01cb310a430c91'}, separators=(',', ':'))
headers = {"Content-type": "application/json",
           "Accept": "text/plain"}
conn = httplib.HTTPConnection("challenge.code2040.org")
conn.request("POST", "/api/haystack", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()

pythonDict = json.loads(data)

def search(pythonDict):
    l = pythonDict.get('needle')
    m = pythonDict.get('haystack')
    for x in m:
        if l == x:
            return m.index(x)


needlePosition = search(pythonDict)

params = json.dumps({'token': '97826876ae83ebe88b01cb310a430c91', 'needle': needlePosition}, separators=(',', ':'))
headers = {"Content-type": "application/json",
           "Accept": "text/plain"}
conn = httplib.HTTPConnection("challenge.code2040.org")
conn.request("POST", "/api/haystack/validate", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()