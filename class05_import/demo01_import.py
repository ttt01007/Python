# 函数 def 函数名()

def say_hello():
    print('hello')

say_hello()
# 传参
def say_hello(num1, num2):
    print(num1 + num2)

say_hello(1, 2)
# 返回值
def say_hello(num1,num2):
    return num1+num2
print(say_hello(2, 2))
# 参数默认值
def say_hello(num1,num2=4):
    return num1+num2
print(say_hello(5))