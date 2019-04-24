from bs4 import BeautifulSoup
import requests


def extract_source():
    headers = {"User-Agent": "Mozilla/5.0"}
    source = requests.get('https://www.crunchbase.com/organization/intel-capital#section-overview', headers=headers).text
    return source


soup = BeautifulSoup(extract_source(), "html.parser")


infor = soup.find("div", class_="section-layout-content")
print(soup.get_text())
