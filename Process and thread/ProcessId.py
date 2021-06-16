# 导入进程包
# 为多个人物分配子进程执行
import multiprocessing
import time
import os


# 唱歌任务
def sing():
    # 获取当前进程编号
    singid = os.getpid()
    print('sing进程ID:', singid)
    # 获取当前进程名称
    sing_name = multiprocessing.current_process()
    print('sing进程名称:', sing_name)
    # 获取当前父进程的编号
    father_singid = os.getppid()
    print()
    # 获取当前父进程名称
    for i in range(3):
        print(f'唱歌中{i}...')
        time.sleep(0.2)


# 跳舞任务
def dance():
    # 获取当前进程编号
    danceid = os.getpid()
    print('dance的进程ID:', danceid)
    # 获取当前进程名称
    dence_name = multiprocessing.current_process()
    print('dance的进程名字:', dence_name)
    for i in range(3):
        print(f'跳舞中{i}...')
        time.sleep(0.2)


# 分配子进程
sing_process = multiprocessing.Process(target=sing)
dance_process = multiprocessing.Process(target=dance)

# 启动进程(进程设置后必须启动才能进行)
sing_process.start()
dance_process.start()
