import asyncio 
import requests 

async def download_image(url):
    #发送网络请求，下载图片(遇到网络下载图片的IO请求,自动化切换到其他任务)
    print('开始下载',url)

    loop = asyncio.get_event_loop()
    #requests模块默认不支持异步操作，所以就使用线程池来配合实现
    future = loop.run_in_executor(None,requests.get,url)

    response = await future 
    print('下载完成')
    #图片保存到本地
    file_name = url.rsplit('/')[-1]
    with open(file_name,'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    url_list = [
    'https://pic.qiushibaike.com/system/pictures/12436/124360753/medium/7TKGSDY0E3FBRC8Q.jpg',
    'https://pic.qiushibaike.com/system/pictures/12437/124377444/medium/JBYNB7E71BC5NYRB.jpg',
    'https://pic.qiushibaike.com/system/pictures/12437/124375149/medium/00EA4WHMKKPFHTJN.jpg'
        ]
    tasks = [download_image(url) for url in url_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))