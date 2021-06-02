import requests
from lxml import etree 
import os 
import random
from multiprocessing.dummy import Pool 
#需求:爬取梨视频的视频数据
headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15(KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'
}
if not os.path.exists('./video'):
    os.mkdir('./video')
#原则:线程池处理的是阻塞且耗时的操作
#对下述url发起请求解析出视频详情页的url和视频的名称 
url = 'https://www.pearvideo.com/category_5'
page_text = requests.get(url=url,headers=headers).text 
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = [] #存储所有视频的链接
for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    #对详情页的url发起请求
    detail_page_text = requests.get(url=detail_url,headers=headers).text
    #通过抓包ajax得到一个可以发送的url和请求伪装的视频的url
    id_ = str(li.xpath('./div/a/@href')[0]).split('_')[1]
    # 可发送请求的url
    ajax_url = 'https://www.pearvideo.com/videoStatus.jsp?'
    params = {
            'contId': id_,
            'mrd': str(random.random())
    }
    ajax_headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3823.400 QQBrowser/10.7.4307.400',
            #防盗链
            'Referer': 'https://www.pearvideo.com/video_' + id_
    }
    # 加了'Referer': 'https://www.pearvideo.com/video_1708144'后就不会显示该视频已下架了
    dic_obj = requests.get(url=ajax_url, params=params, headers=ajax_headers).json()
    video_url = dic_obj["videoInfo"]['videos']["srcUrl"]
    # 此处视频地址做了加密即ajax中得到的地址需要加上cont-,并且修改一段数字为id才是真地址
    # 真地址："https://video.pearvideo.com/mp4/third/20201120/cont-1708144-10305425-222728-hd.mp4"
    # 伪地址："https://video.pearvideo.com/mp4/third/20201120/1606132035863-10305425-222728-hd.mp4"
    
    # 得到真url,做字符串处理
    video_true_url = ''
    s_list = str(video_url).split('/')
    for i in range(0, len(s_list)):
        if i < len(s_list) - 1:
            video_true_url += s_list[i] + '/'
        else:
            ss_list = s_list[i].split('-')
            for j in range(0, len(ss_list)):
                if j == 0:
                    video_true_url += 'cont-' + id_ + '-'
                elif j == len(ss_list) - 1:
                    video_true_url += ss_list[j]
                else:
                    video_true_url += ss_list[j] + '-'
    dic = {
        'name': name,
        'url': video_true_url
    }
    urls.append(dic)
def get_video_data(dic):
    url = dic['url']
    print(dic['name'],'正在下载...')
    data = requests.get(url=url,headers=headers).content
    #持久化存储
    video_path = './video/'+ dic['name']
    with open(video_path,'wb') as fp:
        fp.write(data)
        print(dic['name'],'下载成功！')

#使用线程池对视频数据进行请求                        
pool = Pool(4)
pool.map(get_video_data,urls)

pool.close()
pool.join()