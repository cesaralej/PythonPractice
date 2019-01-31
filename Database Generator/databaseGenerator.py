import random
import json
import csv
import re

SCHOOLS = ["The Spence", "Trinity", "Concord Academy", "The Foxcroft", "Riverdale Country", "The Lawrenceville", "Forman"]
BLOOD = ["AB-negative", "B-negative", "AB-positive", "A-negative", "O-negative", "B-positive", "A-positive", "O-positive"]
DESTINATIONS = ["Madrid", "Athens", "Dubai"]

names = json.loads(open('names.json').read())
father = json.loads(open('fathernames.json').read())
mother = json.loads(open('mothernames.json').read())
lastnames = json.loads(open('apellidso.json').read())


def gen_phone():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))

    return '{}-{}-{}'.format(first, second, last)


def gen_pass():
    passp = ["Colombia"]
    if random.randint(0, 100) > 95:
        passp.append("Italia")
    if random.randint(0, 100) > 95:
        passp.append("USA")
    return passp


with open('database.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['id', 'Name', 'Last Name', 'Phone', 'Email', 'day', 'month', 'year', 'School', 'Insurance Code', 'Blood Type', 'Passports', 'Passport Numbers', 'Destination', 'Father Name', 'Father Phone', 'Mother Name', 'Mother Phone'])
    count = 1
    for name in names:

        firnam = name.split()[0]
        lastn = lastnames[count] + " " + name.split()[1]
        # email = name.replace(" ", "")[0:10] + str(random.randint(0, 999)) + '@hotmail.com'
        # email = name.split()[0][0] + name.split()[1] + str(random.randint(0, 999)) + '@hotmail.com'
        email = name.split()[0][0].lower() + re.sub('[^A-Za-z0-9]+', '', lastnames[count]).lower() + str(random.randint(0, 999)) + '@hotmail.com'
        day = random.randint(1, 31)
        month = random.randint(1, 12)
        year = random.randint(2003, 2005)
        school = random.choice(SCHOOLS)
        insurance = random.randint(1000000, 9999999)
        btype = random.choice(BLOOD)
        passports = gen_pass()
        pnumbers = 0
        dest = random.choice(DESTINATIONS)
        row = [count, firnam, lastn, gen_phone(), email, day, month, year, school, insurance, btype, passports, pnumbers, dest, father[count], gen_phone(), mother[count], gen_phone()]
        csv_writer.writerow(row)
        count += 1
