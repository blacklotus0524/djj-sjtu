import asyncio

async def result(url):
    print("正在请求Url",url)
# async 修饰的函数，调用返回一个协程对象

# 创建事件循环
loop=asyncio.get_event_loop()
loop.run_until_complete(c)

# task
loop=asyncio.get_event_loop()
task=loop.create_task(c)
loop.run_until_complete(task)

# future
loop=asyncio.get_event_loop()
task=asyncio.ensure_future(c)
loop.run_until_complete(task)