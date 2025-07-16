from selenium.webdriver.common.by import By
from utils.browser_actions import BrowserActions

class HomePage:
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Login']")

    def __init__(self, driver):
        self.driver = driver
        self.actions = BrowserActions(driver)

    def go_to_login(self):
        self.actions.click(self.LOGIN_BUTTON)
