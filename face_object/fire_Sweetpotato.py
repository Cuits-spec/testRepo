# 创建地瓜类
class Sweetpost():
# 新建init魔法方法
    def __init__(self):
        # 烤地瓜时间
        self.time = 0
        # 烤地瓜状态
        self.state = '生的'
        # 烤地瓜调料
        self.Seasoning = []
# 封装烤地瓜时间的方法
    def cook_digua(self, time):
        self.time = time
        if self.time>0 and self.time <= 3:
            self.state = '生的'
        elif 3 < self.time <= 5:
            self.state = '半生不熟'
        elif 5 < self.time <= 8:
            self.state = '熟了'
        elif self.time > 8:
            self.state = '烤糊了'
        else:
            self.state = '还没开始烤'
    # 封装str魔法方法会打印返回值
    def __str__(self):
        return f'烤了{self.time}分钟，状态是{self.state}，加的调料有{self.Seasoning}'

    # 封装加调料方法
    def add_Seasoning(self, seasoning):
        self.Seasoning.append(seasoning)

# 实例化类
digua = Sweetpost()
# 调用对象方法
digua.cook_digua(9)
print(digua)
digua.add_Seasoning('胡椒粉')
print(digua)
digua.cook_digua(7)
digua.add_Seasoning('辣椒')
print(digua)