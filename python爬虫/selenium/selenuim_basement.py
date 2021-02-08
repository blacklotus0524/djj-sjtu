# !/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author: Junjie.Ding
# Create time: 2021/2/8

from selenium import webdriver
from lxml import etree
from time import sleep
chrome =webdriver.Chrome(executable_path="./chromedriver")
# 浏览器发起一个指定url的请求
chrome.get("http://scxk.nmpa.gov.cn:81/xk/")

# 获取浏览器当前页面的浏览数据
page_text=chrome.page_source

# 解析企业名称
tree = etree.HTML(page_text)
for li in tree.xpath('//ul[@id="gzlist"]/li'):
    name=li.xpath('./dl/@title')[0]
    print(name)
sleep(5)
chrome.quit()