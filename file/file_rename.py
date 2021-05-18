# 批量修改文件名 设置添加的标识 获取指定目录下所有文件
import os
flag = 1
# 获取指定目录下文件
targer_file = os.listdir('/Users/out/Documents/testRepo/file')
# 遍历目录下的文件列表
# 当flag为1时修改文件名字
# 当flag为2时删除修改的名字
# 重命名打印
