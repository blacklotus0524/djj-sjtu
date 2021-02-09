import time
from multiprocessing.dummy import Pool

start_time=time.time()
def get_page(str):
	print("开始："+str)
	time.sleep(2)
	print("结束："+str)
name_list=["23",'gf','gh','sa']

# 实例化一个线程对象
pool=Pool(2)
# 将列表中每一个元素传递到get_page进行处理

pool.map(get_page,name_list) # map返回值一定是一个列表
end_time=time.time()
print("%.2f second"%(end_time-start_time))










