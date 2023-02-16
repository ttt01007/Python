from selenium import webdriver

ed = webdriver.Edge()
ed.maximize_window()
'''
    弹窗
        1.alert：确认
        2.prompt：支持输入并确认
        3.confirm：确认与取消
'''
# alert弹窗
alert = ed.switch_to.alert
alert.accept()
# confirm弹窗处理
alert.dismiss()
alert.accept()
# prompt
alert.send_keys('13123123')
alert.accept()
alert.dismiss()




ed.close()
