from Crypto.Cipher import AES
from pathlib import Path
import sys
import subprocess
import os
import requests
import time
import re
from selenium.webdriver import Chrome

def get_key(filename):
    with open(filename, 'rb') as f:
        key = f.read()
    return key

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def decrypt_file(filename, key):
    with open("./test/"+filename, 'rb') as f:
        ciphertext = f.read()
    dec = decrypt(ciphertext, key)
    with open('./res/'+filename, 'wb') as f:
        f.write(dec)

def ts2mp4(n):
    file_name = "0.ts"
    for i in range(1, n):
        file_name = file_name + f"+{i}.ts"
    print(os.system("cd res&&copy /b " + file_name + " output.mp4"))
    print(os.system("move D:\\work\\Python\\爬虫\\tecentKeTang\\res\\output.mp4 D:\\work\\Python\\爬虫\\tecentKeTang\\mp4"))
    print(os.system("cd test&&del *.ts"))
    print(os.system("cd res&&del *.ts"))
    print(os.system("del get_dk"))

headers = {
    # 填自己的
}

m3u8_url = input("请输入m3u8链接:")
pattern2 = re.compile(r'(?P<prefix>.*?)voddrm.token.*?exper=0(?P<suffix>.*)',re.S)
res = pattern2.finditer(m3u8_url)
for i in res:
    prefix = i.group("prefix")
    suffix = i.group("suffix")

m3u8_resp = requests.get(m3u8_url,headers=headers)
with open("m3u8","wb") as f:
    f.write(m3u8_resp.content)

pattern1 = re.compile(r'URI="(?P<key>.*?)"')
res = pattern1.finditer(m3u8_resp.text)
for i in res:
    key_url = i.group("key")
key_resp = requests.get(key_url)
with open("get_dk","wb") as f:
    f.write(key_resp.content)
# web = Chrome()
# web.get(key_url)
# time.sleep(5)
# web.close()
key = get_key("get_dk")
# C:/Users/yumu/Downloads/get_dk
print("成功拿到key")
n=0
with open("m3u8","r") as f:
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        single_ts_url = prefix + line + suffix
        # print(single_ts_url)
        single_ts_resp = requests.get(single_ts_url,headers=headers)
        with open(f"./test/{n}.ts","wb") as f:
            f.write(single_ts_resp.content)
        print("下载完成",n+1,"个")
        n=n+1
for i in range(n):
    filename = f"{i}.ts"
    decrypt_file(str(filename), key)
    print("解密完成",i+1,"个")
ts2mp4(n)