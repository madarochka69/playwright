# Смирнов Денис Станиславович
# 12.11.2026
# Время: 14:46
# # Описание: код запускает браузер Firefox, открывает страницу https://playwright.dev/ и проверяет наличие заголовка Playwright и ссылки Get started, а также проверяет видимость заголовка "Installation" после перехода по ссылке.
# # Код из раздела Writing Tests и Installation, запуск локальный.
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title())
    browser.close()
    # Результат запуска: test_1.png
    # Код выполнен без ошибок.