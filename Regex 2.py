import re

import requests
from bs4 import BeautifulSoup as bs


articles_october = requests.get('https://www.kommersant.ru/archive/rubric/4/month/2020-10-01')
soup = bs(articles_october.content)
my_headers = soup.find_all('h3', attrs={'class': 'article_name'})
print(len(my_headers))

all_corona = []
n_res = 0
for header in my_headers:
    if re.search('корона\B|COVID', str(header)):
        n_res +=1
        corona = re.search(r'(?<=>).*(?=<)', str(header)).group()
        all_corona.append(f'{n_res}) {corona}')
print('\n'.join(all_corona))


