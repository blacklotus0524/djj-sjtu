import requests
url="https://pic.qiushibaike.com/system/pictures/12404/124047105/medium/5E0P0O4DSDOX2MO1.jpg"
img_data=requests.get(url=url).content
with open("./qiutu.jpg","wb") as fp:
    fp.write(img_data)