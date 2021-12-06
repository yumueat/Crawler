import requests
from lxml import etree
import csv
f=open("报价.csv",mode="w",encoding='utf-8')
csvwriter=csv.writer(f)
url='https://guiyang.zbj.com/search/f/?kw=saas'
resp=requests.get(url)
html=etree.HTML(resp.text)
divs=html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
dic=[]
for div in divs:
    try:
        com_name=div.xpath('./div/div/a[1]/div[1]/p/text()')[1].strip('\n')
        com_text='saas'.join(div.xpath('./div/div/a[2]/div[2]/div[2]/p/text()'))
        com_price=div.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip('¥')
        dic.append(com_name)
        dic.append(com_text)
        dic.append(com_price)
        csvwriter.writerow(dic)
#       print(com_name,com_text,com_price)
        dic=[]
    except:
        print("有一个错误")


