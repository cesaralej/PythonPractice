from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.bestmytest.com/blog/toefl/toefl-speaking-template')

soup = BeautifulSoup(response.text, 'html.parser')


for num in range(1, 7):
    for h3 in soup.find(id="toefl-speaking-template-task-" + str(num)):
        line = str(h3)

        if line.startswith('<h4>') or line.startswith('<h3>'):
            print(h3.get_text())

        if line.startswith('<div'):

            pos = line.find("<b>", 50)
            templ = BeautifulSoup(line[:pos], 'html.parser')
            print(templ.get_text())

            if line.count("<b>") > 3:
                print('')
                pos2 = line.find("<b>", pos + 50)
                pos3 = line.find("<b>", pos2 + 50)
                templ2 = BeautifulSoup(line[pos2:pos3], 'html.parser')
                print(templ2.get_text())

        print('')
