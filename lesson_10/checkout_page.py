from selenium.webdriver.common.by import By


class CheckoutPage:
    """Page Object страницы оформления заказа."""

    def __init__(self, driver):
        """Инициализировать страницу оформления заказа.

        :param driver: экземпляр Selenium WebDriver.
        """
        self.driver = driver

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """Заполнить данные покупателя.

        :param first_name: имя покупателя.
        :param last_name: фамилия покупателя.
        :param postal_code: почтовый индекс.
        """
        self.driver.find_element(
            By.ID, "first-name"
        ).send_keys(first_name)

        self.driver.find_element(
            By.ID, "last-name"
        ).send_keys(last_name)

        self.driver.find_element(
            By.ID, "postal-code"
        ).send_keys(postal_code)

        self.driver.find_element(
            By.ID, "continue"
        ).click()

    def get_total(self) -> str:
        """Получить итоговую стоимость заказа.

        :return: итоговая стоимость в виде строки.
        """
        return self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        ).text
