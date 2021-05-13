# 创建文件data.txt,文件共100000行，每行存放一个1～100之间的整数
from random import randint
f = open('data.txt', 'w+')
for i in range(100):
    f.write(str(randint(1,99)) + '\n')
f.seek(0)
print(f.read())
f.close()

