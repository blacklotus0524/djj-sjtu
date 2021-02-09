import requests
from lxml import etree
import os
if not os.path.exists("./piclib"):
    os.mkdir("./piclib")
headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
             (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
url="http://www.netbian.com/dongman/"
page_text=requests.get(url=url,headers=headers)
page_text.encoding="gbk"
page_text=page_text.text
tree=etree.HTML(page_text)
img_list=tree.xpath('//div[@class="list"]/ul/li[not(@class="nextpage")]')
for li in img_list:
    if li.xpath('./a/img/@src'):
        img_src = li.xpath('./a/img/@src')[0]
        img_name=li.xpath('./a/img/@alt')[0]+".jpg"
        # 通用处理方法
        # img_name=img_name.encode("iso-8859-1").decode("gbk")

        # print(img_name,img_src)
        img=requests.get(url=img_src,headers=headers).content
        with open("./piclib/"+img_name,"wb") as fp:
            fp.write(img)
        print(img_name+"下载成功")

