import requests
from lxml import etree
import time
import pandas as pd

house_pos = "宝山"
headers = {
	"User-Agent":
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
			 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
house_info_list = []
for page in range(1, 10):
	print("--------------正在爬取第{}页--------------".format(page))
	url = r"https://sh.ke.com/ershoufang/pg{}rs{}/".format(page, house_pos)
	page_text = requests.get(url=url, headers=headers).text
	# 数据解析
	tree = etree.HTML(page_text)
	li_list = tree.xpath('//ul[@class="sellListContent"]//li[@class="clear"]')
	for li in li_list:
		house_info = {}
		house_info['position'] = li.xpath(
			'./div/div[@class="address"]/div[1]/div/a/text()')[0]
		house_info['total_price'] = li.xpath(
			'./div/div[@class="address"]/div[@class="priceInfo"]/div[1]/span/text()'
		)[0]
		house_info['unit_price'] = li.xpath(
			'./div/div[@class="address"]/div[@class="priceInfo"]/div[2]/span/text()'
		)[0]
		house_info['title'] = li.xpath('./div/div[@class="title"]/a/@title')[0]
		house_info_list.append(house_info)
	time.sleep(0.1)

df = pd.DataFrame(house_info_list)
df.to_csv("1.csv")
print("--------------抓取结束--------------")
