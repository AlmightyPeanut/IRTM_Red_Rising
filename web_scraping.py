import os.path

import requests
from bs4 import BeautifulSoup
from pathlib import Path

# _BASE_URL = "https://novel12.com/red-rising/page-1-1946689.htm"
# _BASE_URL = "https://novel12.com/golden-son/page-1-1946795.htm"
_BASE_URL = "https://novel12.com/morning-star/page-1-1946919.htm"
_OUTPUT_FILE = "text_data/raw/red_rising_3.txt"

if __name__ == '__main__':
    url = _BASE_URL

    page_num = 0

    if not os.path.isfile(_OUTPUT_FILE):
        Path(_OUTPUT_FILE).touch()
    with open(_OUTPUT_FILE, "a") as file:
        while True:
            page_num += 1
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')

            text = soup.find("div", class_="content-center").get_text()
            file.write(text)

            button = soup.find_all("a", text="Next >")
            if len(button) == 0:
                break
            url = button[0].get('href')
