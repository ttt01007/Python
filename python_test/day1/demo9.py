from selenium import webdriver
import time

# 启动之前进行配置
eo = webdriver.EdgeOptions()
# 最大化
# eo.add_argument('start-maximized')
# 指定窗口大小的指令
eo.add_argument('windows-size:100,100')
# 指定位置打开浏览器
eo.add_argument('windows-position:100,100')
# 去掉自动化提示
eo.add_experimental_option('excludeSwitches', ['enable-automation'])

# 加载本地缓存，把本地缓存复制一份，准们使用
eo.add_argument(r'--user-data-dir=C:\Users\39884\AppData\Local\Microsoft\Edge\UserD')

# 无UI模式，无头模式
# eo.add_argument('--headless')

# 隐身模式
eo.add_argument('incognito')

# 添加去掉密码弹窗管理
prefs = {}
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
eo.add_experimental_option("prefs",prefs)

ed = webdriver.Edge(options=eo)
ed.get('https://www.csdn.net/')

time.sleep(3)
ed.quit()
