from playwright.sync_api import sync_playwright
import hashlib

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto("https://static.kamept.com/rice",wait_until="networkidle")

    # 等待页面加载完成（关键）
    page.wait_for_timeout(50000)

    content = page.content()

    with open("page.txt", "w") as f:
        f.write(content)

    browser.close()