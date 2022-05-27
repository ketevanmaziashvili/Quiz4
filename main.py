import requests
from bs4 import BeautifulSoup
import sqlite3

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"

}

url = "https://www.worldometers.info/geography/alphabetical-list-of-countries/"
session = requests.session()

try:
    req = session.get(url, headers=headers)
    if req.status_code == 200:
        soup = BeautifulSoup(req.content, "html.parser")
        countries = soup.find("table", {"class": "table-condensed"}).find("tbody").findAll("tr")
        for country in countries:
            print(country.findAll("td")[1].text)

except Exception:
    print("ERORR IN URL ADRESS")



