from selenium import webdriver

from shop_login_page import ShopLoginPage
from shop_main_page import ShopMainPage
from shop_cart_page import ShopCartPage
from shop_checkout_page import ShopCheckoutPage


def test_shop():
    driver = webdriver.Firefox()

    login_page = ShopLoginPage(driver)
    main_page = ShopMainPage(driver)
    cart_page = ShopCartPage(driver)
    checkout_page = ShopCheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    main_page.add_backpack()
    main_page.add_bolt_t_shirt()
    main_page.add_onesie()
    main_page.open_cart()

    cart_page.checkout()

    checkout_page.fill_form(
        "Даша",
        "Шоломок",
        "123456"
    )
    checkout_page.continue_checkout()

    total = checkout_page.get_total()

    driver.quit()

    assert total == "Total: $58.29"
