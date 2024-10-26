from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локаторы
    def login_user_button_locator(self):
        return By.XPATH, '//button//div[text()="Вход"]'

    def login_input_locator(self):
        return By.XPATH, '//input[@id="uid_7"]'

    def password_input_locator(self):
        return By.XPATH, '//input[@id="uid_9"]'

    # Метод для логина
    def login_user(self):
        try:
            # Ожидание и ввод логина
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.login_input_locator())
            )
            login_input = self.find_element(self.login_input_locator())  
            self.send_keys(login_input, "neonila.zinova@icloud.com")  

            # Ожидание и ввод пароля
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.password_input_locator())
            )
            password_input = self.find_element(self.password_input_locator())  
            self.send_keys(password_input, "1809Vika")  

            # Ожидание и нажатие кнопки "Вход"
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.login_user_button_locator())
            )
            self.click(self.login_user_button_locator())
        except Exception as e:
            print(f"Ошибка при логине: {e}")
            self.driver.save_screenshot('login_error.png')
            raise

