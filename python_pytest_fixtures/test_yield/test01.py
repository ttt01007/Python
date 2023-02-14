'''
    1.程序开始执行后，因为test函数中有yield关键字，
    所以test函数并不会真正的执行，二十先得到了一个生成器g
    （相当于一个对象）
    2.知道条用next方法，test函数正式开始执行，先执行test函数中的
    print方法，然后进入到while循环
    3.程序遇到yield关键字，然后把yield当成return，return出了一个8
    程序停止，并没有执行赋值给a的操作，此时next（g)语句执行完成，所以，
    输出的是前2行
    4.程序执行print('****************************')
    5.又开始执行下面的print(next(g))，这个时候是从刚才那个next程序
    停止的地方开始执行的，也就是要执行a的赋值操作，这个时候要注意，这个
    时候赋值操作的右边是没有值的，因为已经return出去了，所以这个时候a
    赋值是none，所以下面的输出是a:None
    6.程序会继续再while里执行，又一次碰到yield，这个时候同样return
    出8，然后程序停止
'''


def test():
    print('begin...')
    while True:
        a = yield 8
        print('a:', a)


g = test()
print(next(g))
print('****************************')
print(next(g))
