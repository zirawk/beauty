import requests
import os
from pathlib import Path
import sys
from bs4 import BeautifulSoup

save_dir = "./img"


def doimgs(bs):
    divs = bs.find_all('div')
    for div in divs:
        # Get img url
        imgs = BeautifulSoup(str(div), features='html.parser').find_all('img')
        if len(imgs) > 0:
            # Download and save
            img_url = imgs[0].get('src')
            resp = requests.get(url=img_url)
            file_name = img_url.split('/')[-1]
            file_path = os.path.join(save_dir, file_name)
            open(file_path, 'wb').write(resp.content)
            print(f'Downloaded: {file_name}')


def doit(u):
    print(f'Parse: {u}')
    html = requests.get(url=u).text
    bs = BeautifulSoup(html, features='html.parser')
    # Find div.content_left
    divs = bs.find_all('div', class_='content_left')
    # Do imgs downloaded
    doimgs(BeautifulSoup(str(divs[0]), features='html.parser'))
    # Get URL of next page
    divs_page = BeautifulSoup(str(divs[1]), features='html.parser').find_all('div', class_='page')
    next_url = 'https://fulitu.me' + BeautifulSoup(str(divs_page[0]), features='html.parser').find_all('a')[-1].get('href')
    # Re-doit!
    if u == next_url:
        return
    else:
        doit(next_url)



first_url = sys.argv[1]
save_dir = os.path.join(save_dir, BeautifulSoup(requests.get(url=first_url).text, features='html.parser').find('h1').string)
print(f'Save to: {save_dir}')
Path(save_dir).mkdir(parents=True, exist_ok=True)
doit(first_url)
print(f'Completed: {save_dir}')
