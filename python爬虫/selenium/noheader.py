# !/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author: Junjie.Ding
# Create time: 2021/2/8
from selenium import webdriver
from time import sleep
from selenium.webdriver import ChromeOptions # 实现规避
from selenium.webdriver.chrome.options import Options

#无可视化界面
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 规避检测
option=ChromeOptions()
option.add_experimental_option("excludeSwitches",['enable-automation'])
chrome=webdriver.Chrome(executable_path="./chromedriver",chrome_options=chrome_options,options=option)
chrome.get("https://www.baidu.com")
page_text=chrome.page_source
print(page_text)
sleep(2)
chrome.quit()