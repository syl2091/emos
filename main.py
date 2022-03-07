import ssl  # ssl验证
import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0'
}



def download(url,name):
    response = requests.get(url).content
    with open("imgs\\"+name+".jpg", 'wb') as f:
        f.write(response)
        f.flush()
        print(name+"写入成功")








res = requests.get('https://www.pkdoutu.com/photo/list/?page=4', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
imgs = soup.select('a>img[data-backup]')
for i in imgs:
    url = i['data-backup']
    name = i['alt']
    download(url,name)





