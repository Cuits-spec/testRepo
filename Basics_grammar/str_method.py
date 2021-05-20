# 将字符串'adcd'转成大写
str1 = 'adcd'
print(str1.upper())

# 计算字符串'cd'在字符串'adcd'中出现的位置
print(str1.find('cd'))

# 用，号分割字符串'a,b,c,d'
str2 = 'a,b,c,d'
print(str2.split(','))

# str3 = 'Python is good' 将Python替换成python
str3 = 'Python is good'
print(str3.lower())

# str4 = 'python修炼第一期.html',写程序从这个字符串中获得.html前面部分，用尽可能多的方法
str4 = 'python修炼第一期.html'
print(str4.replace('.html', ' '))
print(str4.split('.html')) # 返回的是列表
# print(str4.join(' '))

# str5 = 'sajhfkhgksfhjk',获取字符串长度
str5 = 'sajhfkhgksfhjk'
print(len(str5))

# "this is a book",将book替换成apple
str6 = 'this is a book'
print(str6.replace('book', 'apple', 1))

# "this is a book",判断是否以this开头
str7 = 'this is a book'
print(str7.startswith('this'))

# "this is a book",判断是否以apple结尾
str8 = 'this is a book'
print(str8.endswith('apple', 0, 100))

# "this IS a book",将大写字符转化成小写字符
str9 = 'this IS a book'
print(str9.lower())

# "this IS a book",将小写字符转化成大写字符
str10 = 'this IS a book'
print(str10.upper())

# "this is a book\n",删除/n
str11 = 'this is a book'
print(str11.split('\n'))
