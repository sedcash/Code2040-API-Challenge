import httplib
import json

params = json.dumps({'token': '97826876ae83ebe88b01cb310a430c91'}, separators=(',', ':'))
headers = {"Content-type": "application/json",
           "Accept": "text/plain"}
conn = httplib.HTTPConnection("challenge.code2040.org")
conn.request("POST", "/api/prefix", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()

pythonDict = json.loads(data)

def search(pythonDict):
    k = []
    l = pythonDict.get('prefix')
    m = pythonDict.get('array')
    for x in m:
        if l not in x:
            k.append(x)
    return k



arrayWithoutPrefix = search(pythonDict)

params = json.dumps({'token': '97826876ae83ebe88b01cb310a430c91', 'array': arrayWithoutPrefix}, separators=(',', ':'))
headers = {"Content-type": "application/json",
           "Accept": "text/plain"}
conn = httplib.HTTPConnection("challenge.code2040.org")
conn.request("POST", "/api/prefix/validate", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()