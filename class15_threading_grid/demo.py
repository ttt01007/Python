"""
    python的多线程实现
    钓鱼呢threading模块来实现线程的建立
"""
import threading
from time import sleep


# def func_01():
#     for k in range(5):
#         print('01')
#         sleep(1)
#
#
# def func_02():
#     for j in range(5):
#         print('02')
#         sleep(1)
#
#
# # 引入多线程机制
# t1 = threading.Thread(target=func_01())
# t2 = threading.Thread(target=func_02())
# t1.start()
# t2.start()
#
# for i in range(5):
#     print('非线程：{}'.format(i))
#     sleep(1)
