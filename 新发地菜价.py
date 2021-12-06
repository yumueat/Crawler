import requests
import re
import csv
f=open("菜价.csv",mode='w',encoding="utf-8")
cswrite=csv.writer(f)
url='http://www.xinfadi.com.cn/getCat.html'
resp=requests.post(url)
page_content=resp.text
obj=re.compile(r'"id":(?P<id>.*?),"prodName":"(?P<name>.*?)","prodCatid":1186,"prodCat":"(?P<kind>.*?)".*?"lowPrice":"(?P<low>.*?)"'
               r',"highPrice":"(?P<high>.*?)","avgPrice":"(?P<avg>.*?)","place":"(?P<place>.*?)".*?"unitInfo":"(?P<unit>.*?)"',re.S)
ret=obj.finditer(page_content)
dic=[]
for it in ret:
    dic.append(it.group('id'))
    dic.append(it.group('name'))
    dic.append(it.group('kind'))
    dic.append(it.group('low'))
    dic.append(it.group('high'))
    dic.append(it.group('avg'))
    dic.append(it.group('place'))
    dic.append(it.group('unit'))
    cswrite.writerow(dic)
    dic=[]



f.close()
print("over!")