import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location : ')
    if len(address) < 1:
        break
    data = urllib.request.urlopen(address, context = ctx).read()
    dat = data.decode()
    print (f'Retrieving {address}')
    info = json.loads(data)
    print ('Retreived',len(info),'characters')

    sum = 0
    count = 0
    for item in info["comments"]:
        sum = sum + int(item['count'])
        count = count + 1
    print(f'count {count}')
    print(f'sum {sum}')