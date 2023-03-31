from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False, slow_mo=2000)
page = browser.new_page()
page.goto('http://www.baidu.com')
'''
/   从根节点选取
//  从非根节点选取
*   任意节点选取
@   根据属性筛选
text()  根据文本筛选
and 关联属性或者链接文本
[]  可以防止下表/属性/链接文本
/   选取当前节点
..  选取当前节点的父节点
contains    包含
'''

text1 = page.locator('//span[@name="tj_settingicon"]').text_content()
print(text1)

browser.close()

