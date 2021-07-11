import time

import test_03_zz1

import test_03_mo
class Taca001:

    def setup_class(self):
        self.aa = test_03_zz1.Qztj.get_driver()  # 创建的浏览器驱动对象
        self.kk = test_03_mo.YeWu()

    def teardown_class(self):
        self.ss = test_03_zz1.Qztj.get_quit()

    def setup(self):  # 函数级别初始化方法,打开测试网址
        self.aa.get("https://www.xyz.cn/")

    # 函数级别销毁的方法
    def teardown(self):
        pass

    def test_xx1(self):
        self.kk.test_01()
        handles = self.aa.window_handles
        self.aa.switch_to.window(handles[-1])
        a = test_03_zz1.get_test(".pro_all_products")
        assert a == "共65个产品"

    def test_xx2(self):
        self.kk.test_02()
        handles = self.aa.window_handles
        self.aa.switch_to.window(handles[-1])
        a = test_03_zz1.get_test(".pro_all_products")
        assert a == "共31个产品"

    def test_xx3(self):
        self.kk.test_03("健康险")
        a = test_03_zz1.get_test(".hazardC_tit_h1")
        assert a == "相关“健康险”保险产品"


