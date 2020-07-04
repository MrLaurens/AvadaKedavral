from homework.TongLao import TongLao


class XuZhu(TongLao):
    def __init__(self, hp, power):
        super(XuZhu, self).__init__(hp, power)

    def read(self):
        print("罪过罪过")

xz = XuZhu(100,200)
xz.read()