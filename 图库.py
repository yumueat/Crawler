import time
from bs4 import BeautifulSoup
import requests
url='https://www.umei.cc/weimeitupian/'
#headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}
resp=requests.get(url)
resp.encoding='utf-8'
page_content=BeautifulSoup(resp.text,'html.parser')
ret=page_content.find('div',class_='TypeList').find_all('a')
for i in ret:
    href=i.get('href')
    href='https://www.umei.cc/'+href
    child_resp=requests.get(href)
    child_resp.encoding='utf-8'
    child_resp_text=child_resp.text
    child_text=BeautifulSoup(child_resp_text,'html.parser')
    ret2=child_text.find('div',class_="ImageBody")
    src=ret2.find('img')
    img=src.get('src')
    img_resp=requests.get(img)
    img_name ='./img/'+img.split('/')[-1]
    with open(img_name, "wb") as f:
        f.write(img_resp.content)
    print("over!")
print("all over")


