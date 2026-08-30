from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.URL)

    def set_delay(self, delay: int) -> None:
        """Устанавливает задержку вычисления."""
        field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        field.clear()
        field.send_keys(str(delay))

    def click_button(self, value: str) -> None:
        """Нажимает кнопку калькулятора."""
        button = self.driver.find_element(
            By.XPATH,
            f"//span[text()='{value}']"
        )
        button.click()

    def get_result(self) -> str:
        """Ожидает и возвращает результат вычисления."""
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"),
                "15"
            )
        )

        return self.driver.find_element(
            By.CSS_SELECTOR, ".screen"
        ).text
