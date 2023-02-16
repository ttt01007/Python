# 类变量和实例变量的区别
class Tool:
    count = 10

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    def show_count(self):
        print('工具对象的数量{}'.format(self.count))


Tool('1')
Tool('2')
tool3 = Tool('3')
tool3.count = 99
tool4 = Tool('4')
print(tool4.count)
