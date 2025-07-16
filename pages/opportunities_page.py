from datetime import time

from selenium.webdriver.common.by import By
from utils.browser_actions import BrowserActions
from utils.logger import logger


class OpportunitiesPage(BrowserActions):
    def __init__(self, driver):
        super().__init__(driver)  # ✅ Initialize parent
        self.driver = driver

    OPPORTUNITIES_BTN = (By.XPATH, "//span[text()='Opportunities']//parent::a[@id='nav-candidates-opportunities']")
    BADGE = (By.XPATH, "//a[@id='nav-candidates-opportunities']//span[contains(@class,'badge')]")
    BLUE_APPLY_BTN = (By.XPATH, "//div[@ng-controller='candidateOpportunityCtrl']//button[text()='Apply']")
    GREEN_APPLY_BTN = (By.XPATH, "//div[@ng-show='modalParams.showApplyBulkModal']//button[text()='Apply' and not(@disabled)]")
    INTERESTED_BTN = (By.XPATH, "(//button[@id='interested-btn'])[1]")

    def open_opportunities(self):
        self.click(self.OPPORTUNITIES_BTN)

    def get_opportunity_count(self):
        if self.is_element_present(self.BADGE):
            try:
                return int(self.get_text(self.BADGE))
            except Exception as e:
                logger.warning(f"Could not parse opportunity count: {e}")
                return 0
        else:
            logger.info("No opportunity badge found.")
            return 0

    def click_interested_button(self):
        self.click(self.INTERESTED_BTN)

    def apply_to_all(self, count):
        for i in range(count):
            try:
                if self.wait_until_present(self.BLUE_APPLY_BTN):
                    self.click(self.BLUE_APPLY_BTN)

                if self.wait_until_present(self.GREEN_APPLY_BTN):
                    self.click(self.GREEN_APPLY_BTN)
                    logger.info(f"[SUCCESS] Applied to opportunity #{i + 1}")
                else:
                    logger.info(f"[INFO] Green Apply not found for opportunity #{i + 1}")

                # Wait for a second before the next iteration
                time.sleep(1)
            except Exception as e:
                logger.error(f"[ERROR] Opportunity #{i + 1} failed: {str(e)}")
