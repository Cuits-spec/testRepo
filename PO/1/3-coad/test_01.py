import json
import time

from selenium import webdriver


class Driver01:

    #定义一个私有变量存储驱动对象
    __driver = None

    #封装获取驱动对象的方法
    '''
    定义成类级别方法原因：
    1.方便调用
    2.通过类级别方法+判断条件可以保证多次获取驱动对象方法之后只会打开一次浏览器窗口
    '''
    @classmethod
    def get_driver(cls):
        """
        方法封装的套路：
        1.拷贝共性的代码中的其中一份进行实现
        2.修改报错的地方
        3.确认是否需要返回数据

        """
        if cls.__driver is None:
            #创建浏览器驱动对象
            cls.__driver = webdriver.Chrome()
            #窗口最大化
            cls.__driver.maximize_window()
            #隐式等待
            cls.__driver.implicitly_wait(10)

        #返回创建好的驱动对象
        return cls.__driver

    @classmethod
    def driver_quit(cls):
        #为了代码的健壮性，防止没有驱动对象是关闭驱动对象报错问题
        if cls.__driver is not None:
            time.sleep(2)
            cls.__driver.quit()
            #quit的方法只会关闭浏览器窗口，但是不会清楚cls.__driver中存储的值，需要恢复成默认值None
            cls.__driver = None


#封装获取元素文本信息的公用函数
def get_test(xpath):
    time.sleep(2)
    a = Driver01.get_driver().find_element_by_xpath(xpath).text
    time.sleep(2)
    print("实际结果为%s" % a)
    return a


#读取测试数据文件的函数
def get_case_data(lujing):
    #1.先定义一个空列表
    case_data = []
    with open(file = lujing,encoding="utf8") as f: #打开json所在路径的文件赋值给变量f
        #2.读取json中所有数据,赋值给dict_str变量
        dict_str = json.load(f)
        #3.遍历获取所有键值
        for list_data in dict_str.values():  #字典后加.valus是代表值
            #4.获取遍历之后字典的所有键值，追加到空列表case.data中
            case_data.append(list(list_data.values()))
            # print(case_data)

    return case_data
