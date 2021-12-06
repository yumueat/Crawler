import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
f=open("电影.csv",mode="w",encoding="utf-8")
csvwriter=csv.writer(f)
def one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}
    resp=requests.get(url,headers=headers)
    html=etree.HTML(resp.text)
    lis=html.xpath('/ html / body / div[3] / div[1] / div / div[1] / ol / li')
    dic=[]
    for li in lis:
        name=li.xpath('./ div / div[2] / div[1] / a / span[1]/text()')[0]
        point=li.xpath('./ div / div[2] / div[2] / div / span[2]/text()')[0]
        dic.append(name)
        dic.append(point)
        csvwriter.writerow(dic)
        dic=[]


def main():
    with ThreadPoolExecutor(50) as t:
        for i in range(0,9):
            t.submit(one_page, f"https://movie.douban.com/top250?start={i*25}")
    print("all over!")
    pass

if __name__ == '__main__':
    main()