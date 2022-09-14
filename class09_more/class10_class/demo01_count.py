# 类变量和实例变量的区别
class Tool:
    count = 10

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_count(cls):
        print('工具对象的数量{}'.format(cls.count))
