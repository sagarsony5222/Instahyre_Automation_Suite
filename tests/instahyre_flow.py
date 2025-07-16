from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.opportunities_page import OpportunitiesPage
from utils.cred_utils import get_decrypted_credentials
from utils.logger import logger


class TestInstahyreE2E:

    def test_complete_flow(self, browser):
        logger.info("Starting Instahyre E2E test flow.")
        browser.get("https://www.instahyre.com")
        logger.info("Navigated to Instahyre homepage.")
        assert browser.current_url == "https://www.instahyre.com/", "URL Mismatch"
        logger.info("URL verified successfully.")

        # Login
        logger.info("Fetching decrypted credentials.")
        creds = get_decrypted_credentials()
        home = HomePage(browser)
        login = LoginPage(browser)
        logger.info("Navigating to login page.")
        home.go_to_login()
        logger.info("Logging in with provided credentials.")
        login.login(creds["instahyre_email"], creds["instahyre_password"])
        logger.info("Login successful.")

        # Apply to jobs
        logger.info("Navigating to opportunities page.")
        opportunities = OpportunitiesPage(browser)
        opportunities.open_opportunities()
        logger.info("Fetching opportunity count.")
        count = opportunities.get_opportunity_count()
        if count == 0:
            logger.info("No opportunities found. Exiting test early.")
            return  # This will exit the test gracefully

        logger.info(f"Found {count} opportunities.")
        opportunities.click_interested_button()
        logger.info("Starting to apply to all opportunities.")
        opportunities.apply_to_all(count)
        logger.info("Completed applying to all opportunities.")
        browser.quit()
        logger.info("Browser closed.")