import requests
import os 
import aiohttp 
import asyncio 
if not os.path.exists('./pic_as'):
    os.mkdir('./pic_as')
async def fetch(session,url):
    print('发送请求',url)
    async with session.get(url,verify_ssl=False) as response:
        content = await response.content.read()
        file_path = './pic_as/'+ url.rsplit('/')[-1]
        with open(file_path,'wb') as fb:
            fb.write(content)
        print('下载完成:',url)

async def main():
    async with aiohttp.ClientSession() as session:
        url_list = {
        'https://pic.qiushibaike.com/system/pictures/12436/124360753/medium/7TKGSDY0E3FBRC8Q.jpg',
        'https://pic.qiushibaike.com/system/pictures/12437/124377444/medium/JBYNB7E71BC5NYRB.jpg',
        'https://pic.qiushibaike.com/system/pictures/12437/124375149/medium/00EA4WHMKKPFHTJN.jpg'
        }
        tasks = [asyncio.create_task(fetch(session,url)) for url in url_list]
        await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())