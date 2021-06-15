# class Grandfather():
#
#     def __init__(self):
#         self.jianbing = ['古法煎饼果子配方']
#
#     def method(self):
#         print(f'使用{self.jianbing}方法制作煎饼果子')
#
#
# class Father():
#
#     def __init__(self):
#         self.jianbing = ['新生代煎饼果子配方']
#
#     def method(self):
#         print(f'使用{self.jianbing}方法制作煎饼果子')
#
#
# class Son(Father,Grandfather):
#
#     def __init__(self):
#         self.jianbing = ['高科技煎饼果子配方']
#         # super().method()
#     def method(self):
#         print(f'使用{self.jianbing}方法制作煎饼果子')
#
# class Grandson(Father,Grandfather):
#     pass
#
# grandfather = Grandfather()
# father = Father()
# son = Son()
# grandson = Grandson()
# grandson.method()
# # son.method()

# 捕获所有异常描诉信息
try:
    print(num)
except Exception as result:
    print(result)

# 捕获异常描诉信息-起别名的形式
try:
    print(1/0)
except (NameError,ZeroDivisionError) as a:
    print(a)

# 未捕获到异常时的else
try:
    print('哈哈哈')
except Exception as b:
    print(b)
else:
    print('未发现异常')

# 捕获异常之finally
try:
    f = open('test100.txt', 'r')
except Exception as c:
    f = open('test100.txt', 'w')
else:
    print('未捕获到异常时出现')
finally:
    f.close()

# 异常的传递
# 以只读模式打开文件，存在则读取内容，不存在提示用户
# 循环按行读取文件内容，没内容时退出循环，若意外终止则提示用户
import time
try:
    f = open('test100.txt')
    try:
        while True:
            a = f.readlines()
            if len(a) == 0:
                break
            time.sleep(2)
            print(a)
    # control+c可以终止
    except:
        print('程序被意外终止了')
except Exception as e:
    print(e)
    print('该文件不存在！')

# 自定义异常类
# 密码长度少于3位，报自定义异常类并捕获
class CustomError(Exception):
    def __init__(self, user_input, rule_input):
        # 用户输入的密码个数
        self.user_input = user_input
        # 规则指定的需要的密码个数
        self.rule_input = rule_input
    # 设置异常描诉信息
    def __str__(self):
        return f'你输入的密码个数为{self.user_input}，规则限制密码个数必须为{self.rule_input}'
def main():
    try:
        con = input('请输入密码')
        if len(con) < 3:
            raise CustomError(len(con), 3)
    except Exception as r:
        print(r)
    else:
        print('未报错')

main()