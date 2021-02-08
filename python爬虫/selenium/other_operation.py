# !/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author: Junjie.Ding
# Create time: 2021/2/8
from selenium import webdriver
from time import sleep

chrome=webdriver.Chrome(executable_path='./chromedriver')
chrome.get("https://www.taobao.com/")
# 标签定位
search_input=chrome.find_element_by_id('q')
search_input.send_keys("mac")

# execute js
chrome.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(3)
# search button
btn=chrome.find_element_by_css_selector('.btn-search')
btn.click()


chrome.get("https://www.baidu.com")
sleep(2)
chrome.back()

sleep(3)

chrome.quit()