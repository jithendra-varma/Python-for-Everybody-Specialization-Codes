from urllib import request
from bs4 import BeautifulSoup

url = input("Enter the url:")
html = request.urlopen(url).read()
soup = BeautifulSoup(html , 'lxml')

tags = soup('span')
sum = 0
for tag in tags:
    sum = sum+int(tag.contents[0])
print(sum)