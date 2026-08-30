from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object страницы авторизации."""

    def __init__(self, driver):
        """Инициализировать страницу авторизации.

        :param driver: экземпляр Selenium WebDriver.
        """
        self.driver = driver

    def open(self) -> None:
        """Открыть страницу авторизации."""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """Авторизоваться на сайте.

        :param username: имя пользователя.
        :param password: пароль пользователя.
        """
        self.driver.find_element(
            By.ID, "user-name"
        ).send_keys(username)

        self.driver.find_element(
            By.ID, "password"
        ).send_keys(password)

        self.driver.find_element(
            By.ID, "login-button"
        ).click()
