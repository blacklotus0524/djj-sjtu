import requests
import re
import os
if not os.path.exists("./qiutu"):
    os.mkdir('./qiutu')
headers = {
    "User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}
url="https://www.qiushibaike.com/imgrank/"
# 使用通用爬虫对url对应的一整张页面进行爬取
page_txt=requests.get(url=url,headers=headers).text
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
img_src_lit=re.findall(ex,page_txt,re.S)
for src in img_src_lit:
    src="https:"+src
    img_data=requests.get(url=src,headers=headers).content
    img_name=src.split("/")[-1]
    img_path="./qiutu/"+img_name
    with open(img_path,"wb") as fp:
        fp.write(img_data)
        print(img_name,"下载成功")