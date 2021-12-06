import requests
import re
url='https://www.91kanju.com/vod-play/54812-1-1.html'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
resp=requests.get(url,headers=headers)
obj=re.compile(r"url: '(?P<url>.*?)',",re.S)
m3u8_url=obj.search(resp.text).group('url')
# print(m3u8_url)
resp.close()
resp2=requests.get(m3u8_url,headers=headers)
with open("哲仁王后.m3u8",mode='wb') as f:
    f.write(resp2.content)
resp2.close()
# print("over!")
# print(resp.text)
n=1
with open("哲仁王后.m3u8",mode='r',encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if line.startswith('#'):
            continue
        print(line)
        resp3=requests.get(line)
        f=open("哲仁王后/f{n}.ts",mode='wb')
        f.write(resp3.content)
        f.close()
        print("完成一个")
        n+=1


