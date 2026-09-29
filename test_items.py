from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_product_page_has_add_to_basket_button(browser):
    browser.get(link)

    # Для визуальной проверки языка кнопки раскомментируйте паузу:
    # import time; time.sleep(30)

    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(buttons) == 1, "На странице товара должна быть одна кнопка добавления в корзину"
