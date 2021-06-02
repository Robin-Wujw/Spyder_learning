import requests
import os 
if not os.path.exists('./pic'):
    os.mkdir('./pic')
def download_img(url):
    print('开始下载',url)
    #发送网络请求，下载图片
    response = requests.get(url)
    print('下载完成！')
    #图片保存
    file_name = url.rsplit('/')[-1]
    file_path = './pic/' + file_name
    with open(file_path,'wb') as fb:
        fb.write(response.content)
if __name__ == '__main__':
    url_list = [
        'https://pic.qiushibaike.com/system/pictures/12436/124360753/medium/7TKGSDY0E3FBRC8Q.jpg',
        'https://pic.qiushibaike.com/system/pictures/12437/124377444/medium/JBYNB7E71BC5NYRB.jpg',
        'https://pic.qiushibaike.com/system/pictures/12437/124375149/medium/00EA4WHMKKPFHTJN.jpg'
    ]
    for item in url_list:
        download_img(item)