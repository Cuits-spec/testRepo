# 导入线程模块
import threading
import time


def sing():
    # 获取当前线程名称
    sing_thread_name = threading.current_thread()
    print('当前线程名称:', sing_thread_name)
    for i in range(3):
        print('唱歌中...')
        time.sleep(0.2)


def dance():
    # 获取当前线程名称
    dance_thread_name = threading.current_thread()
    print('当前线程名称:', dance_thread_name)
    for i in range(3):
        print("跳舞中...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 获取当前线程名称
    zhu_thread = threading.current_thread()
    print('主线程名称:', zhu_thread)
    # 创建子线程
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)
    # 启用子线程
    sing_thread.start()
    dance_thread.start()
