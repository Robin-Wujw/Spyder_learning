from selenium import webdriver 
from lxml import etree
import time 
#实例化一个浏览器对象(传入浏览器的驱动程序)
bro = webdriver.Chrome(executable_path='./chromedriver')

#编写基于浏览器自动化的操作代码
#让浏览器发起一个制定url对应请求
bro.get('https://www.taobao.com/')
time.sleep(2)
#执行一组js程序
# bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(4)
#点击搜索按钮
#标签定位
search_input = bro.find_element_by_id('q')
#标签交互
search_input.send_keys('小米')
button_input = bro.find_element_by_css_selector('.btn-search')
button_input.click()

bro.get('https://www.baidu.com')
time.sleep(2)
#回退
bro.back()
time.sleep(2)
#前进
bro.forward()
time.sleep(5)
bro.quit()