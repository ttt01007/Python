# lambda表达式
f = lambda a, b, c, d: a * b * c * d
print(f(1, 2, 3, 4))  # 相当于下面这个函数


def test01(a, b, c, d):
    return a * b * c * d


print(test01(1, 2, 3, 4))

g = [lambda a: a * 2, lambda b: b * 3]
print(g[0](5))  # 调用
print(g[1](6))
