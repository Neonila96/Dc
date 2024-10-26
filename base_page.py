import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://discord.com/login'

    def click(self, locator, time=5):
        element = self.find_element(locator, time)
        element.click()

    def hover(self, locator):
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)


    def send_keys(self, locator, text):
        element = self.find_element(locator)  # Найдите элемент по локатору
        element.send_keys(text)  # Введите текст в найденный элемент

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))


    def send_message(self,locator, text_m):
        element = self.find_element(locator)
        element.send_keys(text_m)
        pyautogui.press('enter')
