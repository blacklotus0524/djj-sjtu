# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiubaiproPipeline:
    fp = None
    # 重写父类方法，只在开始爬虫的时候调用一次
    def open_spider(self,spider):
        print('开始爬虫')
        self.fp=open('./qiubai.txt','w',encoding='utf-8')
    # 专门用来处理item对象
    # 接收爬虫文件提交过来的item对象
    # 每接收到一次item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author+':'+content+'\n')

        return item # 传递给下一个即将执行的管道类
    def close_spider(self,spider):
        print('结束爬虫')
        self.fp.close()

# 存储到mysql
class mysqlPileLine:
    conn=None
    cursor=None
    def open_spider(self,spider):
        self.conn=pymysql.Connect(host=,port=,user,password,db)
    def process_item(self,item,spider):
        self.cursor=self.conn.cursor()
        try:
            self.cursor.execute("sql state")
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

# 爬虫文件提交的item类型对象优先提交给优先级较高的管道