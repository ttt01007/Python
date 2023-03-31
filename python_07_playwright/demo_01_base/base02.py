from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,
                                args=['--start-maximized'],
                                slow_mo=3000)
    page = browser.new_page(no_viewport=True)
    page.goto('http://www.zhihu.com')
    page.get_by_text('开通机构号').click()
    # 后退
    page.go_back()
    # 前进
    page.go_forward()
    # 刷新
    page.reload()
    browser.close()
