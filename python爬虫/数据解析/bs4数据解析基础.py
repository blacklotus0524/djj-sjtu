from bs4 import BeautifulSoup
fp=open("./sougou.html","r",encoding="utf-8")
soup=BeautifulSoup(fp,"lxml")
print(soup.find("div"))