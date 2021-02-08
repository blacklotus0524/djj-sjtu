# !/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author: Junjie.Ding
# Create time: 2021/2/8

import asyncio
import time
import aiohttp

start = time.time()
urls=["https://www.baidu.com",'https://www.baidu.com','https://www.baidu.com']

async def get_pages(url):
    print("正在下载",url)
    asyncio.sleep(1)
    async with aiohttp.ClientSession() as session:
        # get,post
        # headers,params/data,proxy="https://xxx.xxxx.xxxx:port"
        async with await session.get(url) as response:
            # text()返回字符串
            # read()二进制
            # json() json
            page_text= await response.text()
            print(page_text)
    print("下载完毕",url)

tasks=[]

for url in urls:
    c=get_pages(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end=time.time()
print(end-start)