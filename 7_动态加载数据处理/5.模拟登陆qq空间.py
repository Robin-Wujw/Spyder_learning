import selenium
import requests
from time import sleep
from selenium import webdriver

bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

username_tag = bro.find_element_by_id('u')
userpasswd_tag = bro.find_element_by_id('p')
username_tag.send_keys('635072437')
sleep(1)
userpasswd_tag.send_keys('Wujiawei_980729')
sleep(1)
login_btn = bro.find_element_by_id('login_button')
sleep(1)
login_btn.click()
sleep(5)
