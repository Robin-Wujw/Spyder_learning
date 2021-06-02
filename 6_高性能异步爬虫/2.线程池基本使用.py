# import time 
# #使用单线程串行方式执行

# def get_page(str):
#     print('正在下载',str)
#     time.sleep(2)
#     print('下载成功',str)
# name_list = ['xiaozi','aa','vv','cc']

# start_time = time.time()
# for i in range(len(name_list)):
#     get_page(name_list[i])

# end_time = time.time()
# print('%d second'%(end_time-start_time))
import time 
#导入线程池对应的类
from multiprocessing.dummy import Pool
#使用线程池方式执行

def get_page(str):
    print('正在下载',str)
    time.sleep(2)
    print('下载成功',str)
name_list = ['xiaozi','aa','vv','cc']
start_time = time.time()
#实例化一个线程池对象
pool = Pool(4)
#将列表中每一个列表元素传递给get_page进行处理
pool.map(get_page,name_list)

end_time = time.time()
print(end_time-start_time)