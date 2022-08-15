import threading
from time import sleep
from selenium import webdriver


def open_123(driver):
    driver.get('http://www.jd.com')
    print(threading.currentThread().name)
    sleep(10)
    driver.quit()


# 定义线程组
th = []

dri1 = webdriver.Edge()
dri2 = webdriver.Edge()
dri3 = webdriver.Edge()

# 引入threading模块
th.append(threading.Thread(target=open_123, args=[dri1]))
th.append(threading.Thread(target=open_123, args=[dri2]))
th.append(threading.Thread(target=open_123, args=[dri3]))
print(open_123(dri1).__name__)

# 所有的线程都需要被手动调用执行
for t in th:
    t.start()

# 定义线程组


# dri1 = webdriver.Edge()
# dri2 = webdriver.Edge()
# dri3 = webdriver.Edge()
#
# # 引入threading模块
# threading.Thread(target=open(), args=[dri1])
# threading.Thread(target=open(), args=[dri2])
# threading.Thread(target=open(), args=[dri3])
