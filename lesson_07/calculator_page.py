from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, delay):
        field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        field.clear()
        field.send_keys(str(delay))

    def click_button(self, value):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']"
        ).click()

    def wait_for_result(self, result):
        return WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"),
                str(result)
            )
        )
