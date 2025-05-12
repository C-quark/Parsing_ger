from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

url = 'https://anylang.net/ru/books/de'

driver = webdriver.Chrome()
driver.get(url)

time.sleep(20)

html = driver.page_source
beautsoup = BeautifulSoup(html, 'html.parser')

links = beautsoup.find_all('a', class_='to_the_book')

for link in links:
    href = link.get('href')
    if href:
        full_href = requests.compat.urljoin(url, href)
        print(full_href)

        res = requests.get(full_href)
        bs = BeautifulSoup(res.text, 'html.parser')

        all_parag = []

        parag = bs.find_all('p')
        for p in parag:
            text = p.get_text(strip=True)
            all_parag.append(text)

        all_text = ' '.join(all_parag)

        with open('books.txt', 'a', encoding='utf-8') as f:
            f.write(f'\n\n=== New Book ===\n\n{all_text}')

        time.sleep(10)

driver.quit()