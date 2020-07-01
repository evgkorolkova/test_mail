from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://mail.yandex.ru/"


    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


    def open(self):
        return self.driver.get(self.url)

