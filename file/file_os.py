import os
# os.mkdir('11')
# os.rmdir('11')
# os.chdir('11') 切换目录
# 打印当前所处目录位置
print(os.getcwd())
# 切换到/Users/out/Documents
os.chdir('/Users/out/Documents')
print(os.getcwd())

file_list = os.listdir('/Users/out/Documents/testRepo/file')
print(file_list)