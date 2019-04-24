import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')

if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_181781.xml' 

print('Retreiving', url)
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)

print(f'Retreived {len(data)} characters')

printcount = 0
sum = 0

counts = tree.findall('.//count')
for count in counts:
  printcount += 1
  sum += int(count.text)

print('Count:', printcount)
print('Sum:', sum)
