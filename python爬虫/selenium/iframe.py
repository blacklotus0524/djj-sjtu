# !/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author: Junjie.Ding
# Create time: 2021/2/8

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
chrome=webdriver.Chrome(executable_path='./chromedriver')
chrome.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# 如果定位的标签在iframe中，则必须进行以下操作进行标签定位
chrome.switch_to.frame('iframeResult')
div=chrome.find_element_by_id('draggable')
# 动作链
action=ActionChains(chrome)
# 点击长按指定标签
action.click_and_hold(div)

for i in range(5):
    action.move_by_offset(17,0).perform()
    sleep(0.2)
# release
action.release()