# !/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author: Junjie.Ding
# Create time: 2021/2/8
import time
import asyncio
async def request(url):
    print("正在下载：",url)
    # 在异步协程中如果出现同步模块相关代码，就无法实现异步
    # time.sleep(1)
    # 遇到阻塞操作必须进行手动刮起
    await asyncio.sleep(2)
    print("下载完毕：",url)
start=time.time()
urls = [
    "www.baidu.com",
    "www.bilibili.com",
    "www.qq.com"
]
stasks=[]#任务列表，存放多个任务对象
for url in urls:
    c=request(url)
    task=asyncio.ensure_future(c)
    stasks.append(task)
loop=asyncio.get_event_loop()
# 需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))
print(time.time()-start)
