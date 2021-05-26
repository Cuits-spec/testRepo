# 定义家具类
class Furniture():
    def __init__(self, name, area):
        # 类属性家具名字和占地面积
        self.name = name
        self.area = area

# 定义房子类
class House():

    def __init__(self, position, area):
        # 添加地理位置属性
        self.position = position
        # 添加占地面积属性
        self.area = area
        # 添加剩余面积属性
        self.surplus = area
        # 家具列表
        self.All_urniture = []

# 定义添加家具方法
    def add_furniture(self, item):
        # 要添加的家具面积<=房间的占地面积才能搬进去
        if self.surplus >= item.area:
            self.All_urniture.append(item.name)
            # 搬进家具后房间的剩余面积
            # item.area -= self.area
            self.surplus -= item.area
        # 添加的家具面积>房间面积时
        else:
            print('面积太大，无法容纳')

    def __str__(self):
        return f'这间房子位于{self.position}，面积{self.area},剩余面积为{self.surplus},家具列表为{self.All_urniture}'

# 实例化对象
shafa = Furniture('沙发', 10)
fangzi = House('北京二环', 1000)
fangzi.add_furniture(shafa)
print(fangzi)