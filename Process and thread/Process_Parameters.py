import multiprocessing


def test1_process(name, age):
    print(name, age)


def test2_process(name, age):
    print(name, age)


# 创建子进程
# 以元组形式传参数，元组里参数顺序要和函数里参数顺序一致
sub1_process = multiprocessing.Process(target=test1_process, args=('张三', 20))
# 以字典形式传参，不必一致
sub2_process = multiprocessing.Process(target=test2_process, kwargs={'age': 20, 'name': '李四'})

# 启动进程
sub1_process.start()
sub2_process.start()


import time

# 定义全局变量
list1 = []

# 定义添加数据方法
def add_data():
    for i in range(5):
        list1.append(i)
        print(i)
        time.sleep(0.2)
    print('添加到列表中的数据：', list1)
# 定义读取数据方法
def read_data():
    print(list1)
# 定义添加任务的进程
add_process = multiprocessing.Process(target=add_data)
# 读取任务的进程
read_process = multiprocessing.Process(target=read_data)

# 启动进程
add_process.start()
# 这个方法是等待add_process这个进程执行完毕后在执行下面的进程
add_process.join()
read_process.start()
# add_process进程往全局变量里添加的数据并没有被read_process进程所读取到，因此得到进程之间不共享全局变量---mian注意的地方别忘了

