import asyncio
from typing import AnyStr 
import requests
import time 
import aiohttp
#使用aiohttp中的ClientSession
start = time.time()
urls = [
    'http://127.0.0.1:5000/robin',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]
async def get_page(url):
    # print('正在下载',url)
    # # #requests.get是基于同步的，必须使用基于异步的网络请求模块进行指定url的请求发送
    # # #aiohttp是基于异步的网络请求模块
    # # response = requests.get(url=url)
    # print('下载完毕',response.text)
    async with aiohttp.ClientSession() as session:
        #get()、post():
        #headers、params/data
        async with await session.get(url=url) as response:
            #text()方法返回字符串形式的响应数据
            #read()方法返回二进制形式的响应数据
            #json()方法返回的是json对象
            #注意：获取响应数据操作之前一定要用await手动挂起
            page_text = await response.text()
            print(page_text)
tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print('总耗时:',time.time()-start)