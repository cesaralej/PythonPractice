# import urllib.request, urllib.parse, urllib.error
# import json

# url = input('Enter location: ')

# if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_181782.json' 

# print('Retreiving', url)
# data = urllib.request.urlopen(url).read().decode()
# info = json.loads(data)

# print(f'Retreived {len(data)} characters')

# printcount = 0
# sum = 0


# for count in info["comments"]:
#   printcount += 1
#   sum += int(count["count"])

# print('Count:', printcount)
# print('Sum:', sum)


import urllib.request, urllib.parse, urllib.error
import json
import ssl


api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        
        continue

    # print(json.dumps(js, indent=4))

    pid = js['results'][0]['place_id']
   
    print('Place id', pid)
    
