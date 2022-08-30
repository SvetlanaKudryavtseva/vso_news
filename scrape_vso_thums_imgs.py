# https://www.youtube.com/watch?v=iUIqPXn4zKs
import requests
from bs4 import BeautifulSoup
# устанавливаем progress bar 
# и затем в коде (for img in imgs:) создаем instance of tqdm and passing imgs

from tqdm import tqdm

baseurl="https://"
url="https://vsoprofil.com/news.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
r = requests.get(url, headers=headers)

content = BeautifulSoup(r.content, "html.parser")
# print(content)

imgs = content.find_all("img")
#print(imgs)

for img in tqdm(imgs):
    img_link = img.attrs.get("src")
    img_full_link = baseurl + img_link
    print(img_full_link)

    ## сами создаем папку cards для наших изображений 

    ## используем requests.get 
    ## передаем туда ссылки img_link
    ## их контент-.content - это image binary format
    ## и присваиваем всё переменной image
    image = requests.get(img_full_link).content

    ## создаем имя файла
    ## rfind ищет в направлении справа на лево первый слеш
    file_name = r"thumbs" + img_full_link[img_full_link.rfind("/"):]
    # print(file_name, img_link)

    ## теперь мы можем открыть файл, используя контекст менеджер
    with open(file_name, "wb") as file:
        file.write(image)


