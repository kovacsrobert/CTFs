import http.client
import ssl

#conn = http.client.HTTPSConnection("challenges.neverlanctf.com", 1120, context = ssl._create_unverified_context())
conn = http.client.HTTPConnection("challenges.neverlanctf.com", 1120)
conn.request("HEAD", "/")
res = conn.getresponse()
print(res.status, res.reason)
data = res.read()
print(data)
conn.close()