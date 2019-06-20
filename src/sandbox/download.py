import requests
from bs4 import BeautifulSoup
import os

URL = "https://movie.douban.com"
SAVE_PATH = "./img/"

# find all target image urls
html = requests.get(URL).text
soup = BeautifulSoup(html, "lxml")
img_ul = soup.find_all("li", {"class", "poster"})

# create folder for save images
os.makedirs(SAVE_PATH, mode=0o777, exist_ok=True)

# download images
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        name = img['alt'].replace(' ', '').replace('.', '_')
        suffix = url.split('.')[-1].replace(' ', '')
        r = requests.get(url, stream=True)
        with open(SAVE_PATH + name + '.' + suffix, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 128):
                f.write(chunk)
        print('Saved '+name)

print("end")
