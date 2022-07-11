from urllib import request
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#optional

import ssl
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    data = request.urlopen(address).read()

    print('Retriving', address)
    print('Retrieved', len(data), 'characters')

    stuff = ET.fromstring(data)

    lst = stuff.findall('comments/comment')
    sum = 0
    count = 0
    for com in lst:
        no = int(com.find('count').text)
        sum = sum + no
        count = count + 1
    print(f'count : {count}')
    print(f'sum : {sum}')