# 一般情况下主进程会等待子进程执行完成后在结束主进程
# 但是若是子进程是个死循环，那主进程就等待不了
# 因此1。设置主进程退出时子进程销毁  -给子进程设置守护主进程
#     2。主进程退出前先销毁子进程

import multiprocessing
import time


def test1():
    # while True:
    for i in range(5):
        print('任务执行中。。')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程
    test1_process = multiprocessing.Process(target=test1)

    # 启动子进程
    test1_process.start()

    time.sleep(2)
    print('主进程结束！')
    # 第二种方法，主进程结束前先销毁子进程
    test1_process.terminate()