# Options封装类
from selenium import webdriver


class Options:
    # @staticmethod
    def conf_options(self):
        # 配置options
        options = webdriver.EdgeOptions()
        # 默认启动窗口最大化
        options.add_argument('start-maximized')
        # 指定窗口大小的指令
        # options.add_argument('windows-size:100,100')
        # 指定位置打开浏览器
        # options.add_argument('windows-position:100,100')
        # 去掉警告条
        # options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 加载本地缓存，把本地缓存复制一份，准们使用
        # options.add_argument(r'--user-data-dir=C:\Users\39884\AppData\Local\Microsoft\Edge\UserD')
        # 无UI模式，无头模式
        # eo.add_argument('--headless')
        # 隐身模式
        # options.add_argument('incognito')
        # 添加去掉密码弹窗管理
        prefs = {}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)

        return options
