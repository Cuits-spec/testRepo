# xx[备份].后缀
user_name = input('请输入要备份的文件名：')
# 找到文件后缀的点
index = user_name.rfind('.')
# print(index)
# 源文件名字
# print(user_name[:index])
# 源文件后面名字
# print(user_name[index:])
new_name = user_name[:index] + '[备份]' +user_name[index:]
# print(new_name)

old_f = open(user_name, 'rb')
new_f = open(new_name, 'wb')

for i in old_f.readlines():
    new_f.write(i)

old_f.close()
new_f.close()

