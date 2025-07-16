from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

class BrowserActions:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, by_locator):
        try:
            self.wait.until(EC.element_to_be_clickable(by_locator)).click()
        except TimeoutException:
            print(f"[Timeout] Element not clickable: {by_locator}")
        except Exception as e:
            print(f"[Error] Click failed: {e}")

    def enter_text(self, by_locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print(f"[Timeout] Element not visible for text input: {by_locator}")
        except Exception as e:
            print(f"[Error] Entering text failed: {e}")

    def get_text(self, by_locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator)).text
        except TimeoutException:
            print(f"[Timeout] Element not visible for getting text: {by_locator}")
            return None
        except Exception as e:
            print(f"[Error] Getting text failed: {e}")
            return None

    def wait_for_visibility(self, by_locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            print(f"[Timeout] Element not visible: {by_locator}")
            return None
        except Exception as e:
            print(f"[Error] Waiting for visibility failed: {e}")
            return None

    def is_element_present(self, by_locator):
        try:
            self.wait.until(EC.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            print(f"[Timeout] Element not present: {by_locator}")
            return False
        except Exception as e:
            print(f"[Error] Checking presence failed: {e}")
            return False

    def refresh(self):
        try:
            self.driver.refresh()
        except Exception as e:
            print(f"[Error] Refresh failed: {e}")

    def go_back(self):
        try:
            self.driver.back()
        except Exception as e:
            print(f"[Error] Going back failed: {e}")

    def go_forward(self):
        try:
            self.driver.forward()
        except Exception as e:
            print(f"[Error] Going forward failed: {e}")

    def switch_to_frame(self, by_locator):
        try:
            frame = self.wait.until(EC.presence_of_element_located(by_locator))
            self.driver.switch_to.frame(frame)
        except TimeoutException:
            print(f"[Timeout] Frame not found: {by_locator}")
        except Exception as e:
            print(f"[Error] Switching to frame failed: {e}")

    def switch_to_default_content(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(f"[Error] Switching to default content failed: {e}")

    def switch_to_window(self, window_handle):
        try:
            self.driver.switch_to.window(window_handle)
        except Exception as e:
            print(f"[Error] Switching to window failed: {e}")

    def close_window(self):
        try:
            self.driver.close()
        except Exception as e:
            print(f"[Error] Closing window failed: {e}")

    def wait_to_page_load(self, timeout=10):
        try:
            self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        except TimeoutException:
            print(f"[Timeout] Page did not load within {timeout} seconds.")
        except Exception as e:
            print(f"[Error] Waiting for page load failed: {e}")

    def scroll_to_element(self, by_locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except TimeoutException:
            print(f"[Timeout] Element not visible for scrolling: {by_locator}")
        except Exception as e:
            print(f"[Error] Scrolling to element failed: {e}")

    def scroll_to_top(self):
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
        except Exception as e:
            print(f"[Error] Scrolling to top failed: {e}")

    def scroll_to_bottom(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            print(f"[Error] Scrolling to bottom failed: {e}")

def wait_until_present(self, by_locator):
    """
    Wait until the element is present in the DOM, regardless of visibility.
    """
    try:
        return self.wait.until(EC.presence_of_element_located(by_locator))
    except TimeoutException:
        self.logger.warning(f"Timeout: Element {by_locator} not present in DOM.")
        return None
    except Exception as e:
        self.logger.error(f"Error waiting for element presence {by_locator}: {str(e)}")
        return None
