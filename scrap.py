import pandas as pd
import numpy as np
from unicodedata import category
from bs4 import BeautifulSoup
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
html_text = requests.get('https://socialblade.com/youtube/top/country/in',headers=headers).text
soup = BeautifulSoup(html_text,'html.parser')
# container3 = soup.find('div',attrs={'style':'float: right; width: 900px;'}).find_all('div',recursive=False)
# print(container3)
container3 = soup.find('div',attrs={'style':'width: 860px; background: #fafafa; padding: 10px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 40px;'})
for con in container3:
    print(con)
    container = con.find_all('div',recursive=False)
    print(container)