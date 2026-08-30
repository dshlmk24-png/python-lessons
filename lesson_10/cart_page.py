from selenium.webdriver.common.by import By


class CartPage:
    """Page Object страницы корзины."""

    def __init__(self, driver):
        """Инициализировать страницу корзины.

        :param driver: экземпляр Selenium WebDriver.
        """
        self.driver = driver

    def checkout(self) -> None:
        """Перейти к оформлению заказа."""
        self.driver.find_element(
            By.ID, "checkout"
        ).click()
