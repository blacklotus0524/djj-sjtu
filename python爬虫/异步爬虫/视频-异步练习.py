# -*- coding:utf-8 -*-
# Author:Junjie.Ding
# time:2021/2/7
import requests
from lxml import etree
import random
from multiprocessing.dummy import Pool
import re

headers = {
	"User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}
url = "https://www.pearvideo.com/category_5"

page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')

video_urls = []  # 存储视频地址和名称
for li in li_list:
	name = li.xpath('./div/a/div[2]/text()')[0]
	v_url = "https://www.pearvideo.com/" + li.xpath('./div/a/@href')[0]
	dic = {
		"name": name,
		"url": v_url
	}
	video_urls.append(dic)


def get_video(dic):
	print("正在爬取" + dic["url"])
	headers_detail = {
		"User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
		"Referer": dic["url"]
	}
	params = {'contId': dic["url"][-7:],
	          "mrd": str(round(random.random(), 16))
	          }
	session = requests.session()
	url_detail = "https://www.pearvideo.com/videoStatus.jsp?"
	response = session.get(url=url_detail, params=params, headers=headers_detail).json()
	data_url = response['videoInfo']['videos']['srcUrl']
	try:
		ex = "third/.*?/(.*?)-.*?"
		# 需要被替换的字符串
		need_replace = re.findall(ex, data_url)[0]
	except:
		ex = "adshort/.*?/(.*?)-.*?"
		# 需要被替换的字符串
		need_replace = re.findall(ex, data_url)[0]
	# 替换后的字符串

	# 真实的下载地址

	replaced = "cont-" + dic["url"][-7:]
	data_url = data_url.replace(need_replace, replaced)
	print(data_url)
	res = requests.get(url=data_url, headers=headers).content
	with open(dic['name'] + ".mp4", "wb") as fp:
		fp.write(res)
	print(dic['name'] + "下载成功")


pool = Pool(4)
pool.map(get_video, video_urls)
pool.close()
pool.join()
