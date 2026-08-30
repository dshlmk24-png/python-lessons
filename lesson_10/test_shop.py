import allure
from selenium import webdriver

from cart_page import CartPage
from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage


@allure.title("Покупка трех товаров")
@allure.description(
    "Проверка оформления заказа из трех товаров."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открыть магазин"):
            login_page.open()

        with allure.step("Авторизоваться"):
            login_page.login(
                "standard_user",
                "secret_sauce"
            )

        with allure.step("Добавить Sauce Labs Backpack"):
            inventory_page.add_product(
                "Sauce Labs Backpack"
            )

        with allure.step("Добавить Sauce Labs Bolt T-Shirt"):
            inventory_page.add_product(
                "Sauce Labs Bolt T-Shirt"
            )

        with allure.step("Добавить Sauce Labs Onesie"):
            inventory_page.add_product(
                "Sauce Labs Onesie"
            )

        with allure.step("Открыть корзину"):
            inventory_page.open_cart()

        with allure.step("Перейти к оформлению заказа"):
            cart_page.checkout()

        with allure.step("Заполнить данные покупателя"):
            checkout_page.fill_form(
                "Даша",
                "Шоломок",
                "123456"
            )

        with allure.step("Получить итоговую стоимость"):
            total = checkout_page.get_total()

        with allure.step("Проверить итоговую стоимость"):
            assert total == "Total: $58.29"

    finally:
        driver.quit()
