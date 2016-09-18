import httplib, json

params = json.dumps({'token': '97826876ae83ebe88b01cb310a430c91', 'github':
    'https://github.com/sedcash/Code2040-API-Challenge'}, separators=(',', ':'))
headers = {"Content-type": "application/json",
           "Accept": "text/plain"}
conn = httplib.HTTPConnection("challenge.code2040.org")
conn.request("POST", "/api/register", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()
