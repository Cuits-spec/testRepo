list1 = [1,2,3,4,5,6]
# 求列表长度
print(len(list1))
# 判断6是否在列表中
print(6 in list1)
# list1 + [7,8,9]结果是什么
list2 = list1 + [7,8,9]
print(list2)
# list1 * 2结果
list3 = list1 * 2
print(list3)
# 求列表元素最大值
print(max(list1))
# 求列表元素最小值
print(min(list1))
# 列表所有元素和
print(sum(list1))
# 在索引1后面新增一个元素10
list1.insert(1, 10)
print(list1)
# 在列表末尾新增一个元素20
list1.append(20)
print(list1)
# list2 = [1,[4,6],True] 将列表里数字修改成原来的2倍
list2 = [1,[4,6],True]
list2[0] = 2
list2[1][0] = 8
list2[1][1] = 12
print(list2)

list3 = [123]
list4 = [456]
list3.extend(list4)
print(list3)

str1 = '123'
str2 = '456'
str3 = str1 + str2
print(str3)

list5 = [2,5,6,7,8,9,2,9,9]
# 找出列表最大值
print(max(list5))
# 找出列表最小值
print(min(list5))
# 找出列表最大值个数
print(list5.count(max(list5)))
# 计算列表所有元素和
print(sum(list5))
# 计算列表元素平均值
print(sum(list5)/len(list5))
# 计算列表长度
print(len(list5))
# 找出元素6在列表的索引
print(list5.index(6))
