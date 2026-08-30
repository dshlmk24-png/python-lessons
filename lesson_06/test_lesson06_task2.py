from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")
    cookie_user_1 = {
        "name": "yandex_login",
        "value": "elobuh"
    }
    driver.add_cookie(cookie_user_1)
    driver.refresh()
    driver.get("https://gitflic.ru/user/elobuh")
    user_1_url = driver.current_url
    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")
    cookie_user_2 = {
        "name": "yandex_login",
        "value": "dshlmk"
    }
    driver.add_cookie(cookie_user_2)
    driver.refresh()
    driver.get("https://gitflic.ru/user/dshlmk")
    user_2_url = driver.current_url
    assert user_1_url != user_2_url
    driver.quit()
