import threading
from time import sleep
from selenium import webdriver


def open(driver):
    driver.get('http://www.baidu.com')
    print(threading.currentThread().name)
    sleep(5)
    driver.quit()


# 定义线程组
th = []

dri1 = webdriver.Edge().get('http://www.baidu.com')
dri2 = webdriver.Edge().get('http://www.baidu.com')
dri3 = webdriver.Edge().get('http://www.baidu.com')

# 引入threading模块
th.append(threading.Thread(target=open(), args=[dri1]))
th.append(threading.Thread(target=open(), args=[dri2]))
th.append(threading.Thread(target=open(), args=[dri3]))

# 所有的线程都需要被手动调用执行
# for t in th:
#     t.start()

# 定义线程组


# dri1 = webdriver.Edge()
# dri2 = webdriver.Edge()
# dri3 = webdriver.Edge()
#
# # 引入threading模块
# threading.Thread(target=open(), args=[dri1])
# threading.Thread(target=open(), args=[dri2])
# threading.Thread(target=open(), args=[dri3])
