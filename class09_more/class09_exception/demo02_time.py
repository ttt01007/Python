import time

# 当前时间戳
print('当前时间戳：', time.time())
# 时间戳转时间元组  time.time() 可以省略
print('时间元组：', time.localtime(time.time()))
# 时间元组 转成 正常时间格式 time.localtime() 可以省略
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# 时间元组转成 时间戳
print(time.mktime(time.localtime()))
# 将一个时间戳转化为UTC时区（0时区）的struct_time
print(time.gmtime(time.time()))
