# 闭包
# 形成条件：
# 1.实现函数嵌套
# 2.内部函数使用外部函数的变量
# 3.外部函数返回内部函数

# 闭包的作用：闭包可以保存外部函数的变量，直接给内部函数去调用，不会因为外部函数调用完而销毁

# 外部函数
# def do_test(c):
#     b = 10
#
#     # 内部函数
#     def test2(a):
#         print(a, b, c)
#
#     # 外部函数返回
#     return test2
#
#
# f = do_test(3)
# f(2)


# 装饰器
# def check(fc):
#     print('装饰器函数执行')
#
#     def inner():
#         # 2
#         print('请先登录')
#         fc()
#
#     return inner
#
#
# def talk():
#     print('发表言论')
#
#
# a=check(talk)
# a()

# 装饰器
def check(fc):
    print('装饰器函数执行')

    def inner():
        # 2
        print('请先登录')
        fc()

    def inner2():
        print('zaicidenglu')
        fc()

    return inner


@check
def talk():
    print('发表言论')


talk()
