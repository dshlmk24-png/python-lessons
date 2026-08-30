import allure
from selenium import webdriver

from calculator_page import CalculatorPage


@allure.title("Проверка работы калькулятора")
@allure.description(
    "Проверка сложения 7 и 8 с задержкой 45 секунд."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    driver = webdriver.Chrome()

    try:
        page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            page.open()

        with allure.step("Установить задержку 45 секунд"):
            page.set_delay(1)

        with allure.step("Нажать кнопку 7"):
            page.click_button("7")

        with allure.step("Нажать кнопку +"):
            page.click_button("+")

        with allure.step("Нажать кнопку 8"):
            page.click_button("8")

        with allure.step("Нажать кнопку ="):
            page.click_button("=")

        with allure.step("Проверить результат"):
            result = page.get_result()
            assert result == "15"

    finally:
        driver.quit()
