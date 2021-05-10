dict1 = {'python': 95, 'java': 99, 'c': 100}
# 字典长度为多少
print(len(dict1))
# 修改'java'这个key对应的value值为98
dict1['java']=98
print(dict1)
# 删除 c 这个key
del dict1['c']
print(dict1)
# 增加一个key-value对，key值为php，value为90
dict1['php'] = 90
print(dict1)
# 获取所有key值，存储在列表里
print(dict1.keys())
# 获取所有value值，存储在列表里
print(dict1.values())
# 判断JavaScript是否在字典里
result = 'javaScript' in dict1
print(result)
# 获取字典所有value和
#for value in dict1.values():
list = list(dict1.values())
print(sum(list))
# 获取字典中最大的value值
print(max(list))
# 获取字典中最小的value值
print(min(list))
# 字典dict2 = {'php':97}，将dict2数据更新到dict1中
dict1['php'] = 97
print(dict1)
dict2 = {'css': 99}
dict1.update(dict2)
print(dict1)