# video https://www.youtube.com/watch?v=nCuPv3tf2Hg&list=PLRzwgpycm-Fio7EyivRKOBN4D3tfQ_rpu
# по видео не получилось вывести все продукты
# похожая на видео статья, добавился модуль pandas
# https://www.freecodecamp.org/news/scraping-ecommerce-website-with-python/

from dataclasses import field
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

baseurl = "https://"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
product_links = []
t={}
c=0
for x in range(1):
    r = requests.get('https://vsoprofil.com/news.html'.format(x)).text
    content = BeautifulSoup(r,'html.parser')
    product_list = content.find_all("td",{"width":"220px"})
    #print(product_list)
    for product in product_list:
        for link in product.find_all("a", href=True):
            product_links.append(baseurl + link['href'])
#print (len(product_links))

## для одной новости раскомментировать строчку ниже
test_link = 'https://vsoprofil.com/news/magazin_strojmaterialy_domodedovo'
## для одной новости раскомментировать строчку ниже и убрать строчки для всех новостей и индент
rr = requests.get(test_link, headers=headers)
## для всех новостей раскомментировать и сделать индент
# for news in test_link:
    # try:
    #     rr = requests.get(news, headers=headers)
    # except requests.exceptions.ConnectionError:
    #     print("Max retries exceeded")
soup = BeautifulSoup(rr.text,'html.parser')
stat = soup.find('div', {'id':'stat'})
text = soup.find('div', {'id':'stat'}).text
try:
    title = soup.find('h1').text.strip()
except:
    title = None
#print(title)
images_box = soup.find('div', attrs={'id': 'stat'})
imgs = images_box.find_all("img", {'width': True})
#print(len(imgs))
#print(imgs)
# for img in imgs:
#     img_link = baseurl + img.attrs.get("src")
#     print(img_link)
#     image = requests.get(img_link).content
#     file_name = r"news" + img_link[img_link.rfind("/"):]
#     #print(file_name, img_link)

#     ## теперь мы можем открыть файл, используя контекст менеджер
#     with open(file_name, "wb") as file:
#         file.write(image)

one_news = {
    'title': title,
    'text': text,
}
#print(one_news['title'])
with open('data.csv', 'w', encoding='cp1251', newline='') as f:
    column_headers = ['title', 'text']
    thewriter = csv.DictWriter(f, fieldnames=column_headers, delimiter=";")
    thewriter.writeheader()
    thewriter.writerow(one_news)

