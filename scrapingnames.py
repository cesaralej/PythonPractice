import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
if len(url) < 1:
  url = 'http://py4e-data.dr-chuck.net/known_by_Cameryn.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


count = int(input('Enter count: '))
position = int(input('Enter position: '))

tags = soup('a')

for repeat in range(count):
  url = tags[position-1].get('href', None)
  html = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  print('Retreiving:', url)




