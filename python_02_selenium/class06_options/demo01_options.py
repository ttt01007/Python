'''
    启动浏览器之前的配置选项
        1.最大化
        2.去掉警告条
        3.加载本地缓存
'''
from selenium import webdriver

# 配置options
from python_selenium.class06_options.demo02_edge_options import Options

# options = webdriver.EdgeOptions()
# # 默认启动窗口最大化
# # options.add_argument('start-maximized')
# # 指定窗口大小的指令
# options.add_argument('windows-size:100,100')
# # 指定位置打开浏览器
# options.add_argument('windows-position:100,100')
# # 去掉警告条
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# # 加载本地缓存，把本地缓存复制一份，准们使用
# # options.add_argument(r'--user-data-dir=C:\Users\39884\AppData\Local\Microsoft\Edge\UserD')
# # 无UI模式，无头模式
# # eo.add_argument('--headless')
# # 隐身模式
# options.add_argument('incognito')
# # 添加去掉密码弹窗管理
# prefs = {}
# prefs["credentials_enable_service"] = False
# prefs["profile.password_manager_enabled"] = False
# options.add_experimental_option("prefs", prefs)

driver = webdriver.Edge(options=Options().conf_options())
# driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
text = driver.find_element('xpath', '//*[@id="s-top-loginbtn"]').text
driver.close()
