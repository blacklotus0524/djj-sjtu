import asyncio

async def result(url):
    print("正在请求Url",url)
# async 修饰的函数，调用返回一个协程对象
c=result("www.baidu.com")
# # 创建事件循环
# loop=asyncio.get_event_loop()
# loop.run_until_complete(c)

# # task
# loop=asyncio.get_event_loop()
# task=loop.create_task(c)
# loop.run_until_complete(task)

# # future
# loop=asyncio.get_event_loop()
# task=asyncio.ensure_future(c)
# loop.run_until_complete(task)

def callback_func(task):
    print(task.result())
# 绑定回调
loop=asyncio.get_event_loop()
task=asyncio.ensure_future(c)
# 将回调函数绑定到人物对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)
