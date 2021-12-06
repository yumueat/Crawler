import requests
url="https://desktop.github.com/images/star-bg.svg"
resp=requests.get(url)
# print(resp.text)
with open("github_bg","wb") as f:
    f.write(resp.content)