from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для кнопки "Вход"
    def login_user_button_locator(self):
        return By.XPATH, '//button//div[text()="Вход"]'

    # Локатор для ввода логина
    def login_input_locator(self):
        return By.XPATH, '//input[@id="uid_7"]'

    # Локатор для ввода пароля
    def password_input_locator(self):
        return By.XPATH, '//input[@id="uid_9"]'

    # Метод для залогиниться
    def login_user(self):
        try:
            # Ожидание появления поля ввода логина
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.login_input_locator())
            )
            self.send_keys(self.login_input_locator(), "neonila.zinova@icloud.com")

            # Ожидание появления поля ввода пароля
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.password_input_locator())
            )
            self.send_keys(self.password_input_locator(), "1809Vika")

            # Ожидание появления кнопки "Вход"
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.login_user_button_locator())
            )
            self.click(self.login_user_button_locator())
        except Exception as e:
            print(f"Ошибка при логине: {e}")
            self.driver.save_screenshot('login_error.png')
            raise

    # Метод для открытия страницы
    def open_login_page(self):
        self.open_page()
