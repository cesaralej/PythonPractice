import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')

if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_181782.json' 

print('Retreiving', url)
data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)

print(f'Retreived {len(data)} characters')

printcount = 0
sum = 0


for count in info["comments"]:
  printcount += 1
  sum += int(count["count"])

print('Count:', printcount)
print('Sum:', sum)
