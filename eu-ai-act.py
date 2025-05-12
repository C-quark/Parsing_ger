import requests
from bs4 import BeautifulSoup

url = 'https://huggingface.co/blog/eu-ai-act-for-oss-developers'

response = requests.get(url)
beautsoup = BeautifulSoup(response.text, 'html.parser')

contents = beautsoup.select('div.max-lg.overflow-hidden > b, em, span, p, th')
content = []

for i in contents:
    content.append(i.text.strip())

all_content = '\n\n'.join(content)

with open('eu-ai-act.txt', 'w', encoding='utf-8') as f:
    f.write(all_content)


