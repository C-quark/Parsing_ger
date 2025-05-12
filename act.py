import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://artificialintelligenceact.eu/ai-act-explorer/'

table = {'Inf': [], 'Article': [], 'Content': []}

response = requests.get(url)
beautsoup = BeautifulSoup(response.text, 'html.parser')

links = beautsoup.select('p.child-article > a')
if not links:
    exit()

for link in links:
    href = link.get('href')
    if href:
        full_href = requests.compat.urljoin(url, href)

        res = requests.get(full_href)
        bs = BeautifulSoup(res.text, 'html.parser')

        blocks = bs.find_all('p', class_='aia-eif-value')
        inf = []

        for block in blocks:
            inf.append(block.text)

        article = bs.find_all('h1', class_='entry-title')
        art = []

        for ar in article:
            art.append(ar.text)

        contents = bs.find_all('div', class_='et_pb_module et_pb_post_content et_pb_post_content_0_tb_body')
        content = []

        for con in contents:
            content.append(con.text)

        table['Inf'].append(' '.join(inf))
        table['Article'].append(' '.join(art))
        table['Content'].append(' '.join(content))

df = pd.DataFrame(table)
df.to_csv('act.csv', index=False)