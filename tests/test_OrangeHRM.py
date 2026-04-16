import pytest
from pages.login_page import LoginPage
from utils.logger import Logger
from config.config import Config

logger = Logger().get_logger()

class TestLogin:
    """Test class for OrangeHRM Login functionality"""
    
    def test_login_logout(self, driver):
        """
        Test Case: Login and Logout flow
        Steps:
        1. Open URL
        2. Maximize window and refresh
        3. Enter username and password
        4. Click on submit button
        5. Once logged in, sleep 5 seconds then logout
        """
        logger.info("=" * 50)
        logger.info("Starting test_login_logout")
        logger.info("=" * 50)
        
        # Initialize page object
        login_page = LoginPage(driver)
        
        # Step 1 & 2: Open URL, maximize and refresh
        logger.info("Step 1-2: Opening URL, maximizing window and refreshing")
        login_page.open_login_page(Config.BASE_URL)
        
        # Step 3 & 4: Enter credentials and click login
        logger.info("Step 3-4: Entering credentials and clicking login")
        login_page.do_login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        
        # Verify login is successful
        assert login_page.is_login_successful(), "Login failed - Profile dropdown not found"
        logger.info("Login verification passed")
        
        # Step 5: Wait 5 seconds and logout
        logger.info("Step 5: Performing logout")
        login_page.do_logout()
        
        logger.info("Test completed successfully")
        logger.info("=" * 50)
