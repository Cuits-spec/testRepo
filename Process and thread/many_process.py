# 导入进程包
# 为多个人物分配子进程执行
import multiprocessing
import time


# 唱歌任务
def sing():
    for i in range(3):
        print(f'唱歌中{i}...')
        time.sleep(0.2)


# 跳舞任务
def dance():
    for i in range(3):
        print(f'跳舞中{i}...')
        time.sleep(0.2)


# 分配子进程
sing_process = multiprocessing.Process(target=sing)
dance_process = multiprocessing.Process(target=dance)

# 启动进程(进程设置后必须启动才能进行)
sing_process.start()
dance_process.start()
