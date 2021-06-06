import selenium
import requests
from time import sleep
from selenium import webdriver
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
#实现规避检测
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

#实现无可视化界面的操作
#实现规避检测
option = ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_experimental_option('excludeSwitches',['enable-automation'])
#如何实现让selenium规避被检测到的风险
bro = webdriver.Chrome(executable_path='./chromedriver',options=option)

#无可视化界面(无头浏览器) phantomJS
bro.get('https://www.baidu.com')
print(bro.page_source)
sleep(2)
bro.quit()