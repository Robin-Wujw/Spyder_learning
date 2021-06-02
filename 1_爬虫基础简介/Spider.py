import requests
from requests.exceptions import RequestException
import re
import json 
import time 
def get_one_page(url):
    try:
        headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15(KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
        'Cookie': '__mta=251933366.1621651288799.1621654652344.1621659714789.6; uuid_n_v=v1; uuid=355108E0BAA711EB928335A9BF2872B941E6AF7263AD48DE8E8216997BDA0DAE; _lxsdk_cuid=17991f2f254c8-065fbf94d2f0a5-3f740859-13c680-17991f2f254c8; _lxsdk=355108E0BAA711EB928335A9BF2872B941E6AF7263AD48DE8E8216997BDA0DAE; _csrf=86dc8805803cbb7bebc312dbc0b722ea5b8c1e824740dbe3258724f129c745ef; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1621651289,1621659715; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1621659715; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; _lxsdk_s=17992738487-4fd-b96-39e||2'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None 
    except RequestException:
        return None 
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:],
            'time' : item[4].strip()[5:],
            'score': item[5] + item[6]
        }
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
def main(offset):
    url = 'http://maoyan.com/board/4' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
if __name__ == '__main__':
    for i in range(10):
        main(offset = i*10)
        time.sleep(1)
