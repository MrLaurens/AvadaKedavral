class CaiXuKun:  # 定义一个蔡徐坤
    def __init__(self, height, weight):  # 传入身高体重参数
        self.height = 184
        self.weight = 60

    def skill(self):  # 定义他的技能，唱跳rap篮球
        print(f"我是蔡徐坤，身高{self.height}cm,体重{self.weight}kg,会唱、跳、rap、篮球")

    def sing(self):  # 定义一个成名曲
        print("鸡你太美！")


import time


# 导入时间包

class WuYiFan:  # 定义一个吴亦凡
    def __init__(self, nation, birthday):  # 传入国籍和生日参数
        self.nation = "Canada"
        self.birthday = time.asctime(1990, 11, 6)

    def dawankuanmian(self):  # 大碗宽面就不用我说了吧
        print("从不敢去相信，大碗能让你开心~")


import random


# 导入随机包

class Dinner:  # 定义一个晚饭
    def function(self):  # 不知道吃什么的时候，随机一下
        print("今晚吃{}".format(str(random.choice(["粥", "粉", "面", "饭"]))))


class Bag:  # 定义一个包包
    def __init__(self, color, capacity):  # 需要传入颜色和容量
        self.color = color
        self.capacity = capacity

    def carry(self):  # 调用前面传入定义的颜色和容量参数
        print(f"我在背{self.color}色，容量{self.capacity}L的包包")


import math


# 导入科学数学包
class WirelessEarphone:  # 定义无线耳机
    def __init__(self, volume):  # 需要传入当前电量
        self.volume = volume

    def get_volume(self):  # 获取当前耳机电量
        print(f"当前剩余电量为{self.volume}")

    def battery(self, batteryvolume):  # 无线耳机电池仓的电量
        self.batteryvolume = batteryvolume

    def playtime(self):  # 计算续航时间，假设100电量能跑一个循环
        print("可以循环充电使用{}次".format(math.floor((self.volume + self.batteryvolume) / 100)))
