import requests
from bs4 import BeautifulSoup
import time


url="https://www.shicimingju.com/book/sanguoyanyi.html"
header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
page_text=requests.get(url=url,headers=header)
page_text.encoding="UTF-8"
page_text=page_text.text
#实例化bs对象
soup=BeautifulSoup(page_text,"lxml")

# 解析章节标题
fp=open("./sanguo.txt",'w',encoding="utf-8")
li_list =soup.select(".book-mulu > ul > li")
for li in li_list:
    title=li.a.string
    detail_url="https://www.shicimingju.com/"+li.a["href"]
    # 对详情页发送请求
    detail_page_text=requests.get(url=detail_url,headers=header)
    detail_page_text.encoding="UTF-8"
    detail_page_text=detail_page_text.text
    detail_soup=BeautifulSoup(detail_page_text,"lxml")
    div_tag=detail_soup.find("div", class_="chapter_content")
    content=div_tag.text
    fp.write(title+":"+content+"\n")
    print(title,"爬取成功")
    time.sleep(1)

