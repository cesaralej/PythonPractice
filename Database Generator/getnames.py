from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.saberespractico.com/curiosidades/apellidos-mas-comunes-en-espana/')

soup = BeautifulSoup(response.text, 'html.parser')
fi = open('apellidso.json', 'w')
table = soup.find_all('table')[1].find_all('tr')
fi.write('[')

for h3 in table[1:]:
    fi.write('"' + h3.find_all('td')[1].get_text().capitalize() + '",')
    # print('"' + h3.find_all('td')[1].get_text().capitalize() + '",')

fi.write(']')
