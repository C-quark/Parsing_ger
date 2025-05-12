import requests
from bs4 import BeautifulSoup

url = 'https://www.bundesregierung.de/breg-de/aktuelles/ai-act-2285944'

response = requests.get(url)
beautsoup = BeautifulSoup(response.text, 'html.parser')

titles = beautsoup.find('span', class_='bpa-teaser-title-text-inner')
title = titles.text.strip()

contents = beautsoup.select('div.bpa-richtext > p, h2')
content = []

for c in contents:
    content.append(c.text.strip())

all_content = '\n\n'.join(content)

with open('rules.txt', 'w', encoding='utf-8') as f:
    f.write(f'{title}\n\n')
    f.write(all_content)



