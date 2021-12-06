import asyncio
import requests
import aiohttp
import json
import aiofiles
from lxml import etree
# https://boxnovel.baidu.com/boxnovel/content?gid=4306063500&data={"fromaction":"dushu"}&cid=11348571
# /html/body/div/main/div[2]/div[2]/main/div/div[1]/p
# /html/body/div/main/div[2]/div[2]/main/div/div[2]/p
async def get_book(cid):
    url='https://boxnovel.baidu.com/boxnovel/content?gid=4306063500&data={"fromaction":"dushu"}&cid='+cid
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text=await resp.text()
            print(text)
            html = etree.HTML(text)
            divs = html.xpath('/html/body/div/main/div[2]/div[2]/main/div/div')
            for div in divs:
                print(1)
                book_content=div.xpath('./p/text()')
                print(book_content)
            print("over!")
    pass
# async def make_point():
#     tasks=[]
#     for i in range(1,2):
#         cid=11348570+i
#         tasks.append(get_book(str(cid)))
#     await asyncio.wait(tasks)
#     pass
if __name__ == '__main__':
    # asyncio.run(make_point())
    for i in range(1, 3):
        cid=11348570+i
        loop=asyncio.get_event_loop()
        loop.run_until_complete(get_book(str(cid)))

