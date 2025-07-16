from selenium.webdriver.common.by import By
from utils.browser_actions import BrowserActions

class LoginPage:
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Login']")

    def __init__(self, driver):
        self.driver = driver
        self.actions = BrowserActions(driver)

    def login(self, email, password):
        self.actions.enter_text(self.EMAIL_FIELD, email)
        self.actions.enter_text(self.PASSWORD_FIELD, password)
        self.actions.click(self.SUBMIT_BUTTON)
