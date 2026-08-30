from selenium.webdriver.common.by import By


class InventoryPage:
    """Page Object главной страницы магазина."""

    def __init__(self, driver):
        """Инициализировать страницу магазина.

        :param driver: экземпляр Selenium WebDriver.
        """
        self.driver = driver

    def add_product(self, product_name: str) -> None:
        """Добавить товар в корзину.

        :param product_name: название товара.
        """
        product = self.driver.find_element(
            By.XPATH,
            f"//div[text()='{product_name}']"
        )

        product.find_element(
            By.XPATH,
            "./ancestor::div[@class='inventory_item']"
            "//button"
        ).click()

    def open_cart(self) -> None:
        """Открыть корзину."""
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
