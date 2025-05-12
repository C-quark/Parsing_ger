import requests
from bs4 import BeautifulSoup

url = 'https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689'

response = requests.get(url)
beautsoup = BeautifulSoup(response.text, 'html.parser')

titles = beautsoup.find(id='tit_1')
title = titles.text

information = beautsoup.find_all('p', class_='oj-normal')
inf = []

for p in information:
    inf.append(p.text)

all_inf = ' '.join(inf)

with open('eur-lex.txt', 'w', encoding='utf-8') as f:
    f.write(f'{title}\n\n')
    f.write(all_inf)


