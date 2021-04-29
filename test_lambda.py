fu0 = lambda a : a
print(fu0('hello python'))

fu1 = lambda : 100
print(fu1())

fu2 = lambda a,b:a + b
print(fu2(1,2))

fu3 = lambda a,b,c=100:a+b+c
print(fu3(1,2,3))
print(fu3(1,2))

# *args:args 可变参数返回的是一个元祖
fu4 = lambda *args:args
print(fu4(10,30,50,'kkk'))

# 返回字典
fu5 = lambda **kwargs:kwargs
print(fu5(name=10,age=30))


