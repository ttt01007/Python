# 异常
try:
    int(input('输入数字：'))
except ZeroDivisionError as e:
    print('0除数')
except Exception as e:
    print('未知错误%s' % e)
else:
    print('没有异常的代码')
finally:
    print('结束')


def input_pwd():
    pwd = input('请输入密码：')
    if len(pwd) >= 8:
        return pwd
    exx = Exception('密码长度不够')
    raise exx


print(input_pwd())
