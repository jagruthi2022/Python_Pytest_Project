import pytest
from pages.amazon_login import AmazonLoginPage
from utils.logger import Logger
from config.config import Config

logger = Logger().get_logger()

class TestAmazonUrl:
    """This testcase will verify the URL and login functionality of Amazon website"""
    
    def test_amazon_url(self, driver):
        """
        Test Case: Verify Amazon URL and Login functionality
        Steps:
        1. Open Amazon URL
        2. Maximize window and refresh
        3. Verify the URL is correct
        """
        logger.info("=" * 50)
        logger.info("Starting test_amazon_url")
        logger.info("=" * 50)

        # Initialize page object
        amazon_page = AmazonLoginPage(driver)

        # Step 1 & 2: Open URL, maximize and refresh
        logger.info("Step 1-2: Opening Amazon URL, maximizing window and refreshing")
        amazon_page.open_amazon_page(Config.AMAZON_URL)

        # Step 3: Verify the URL is correct
        current_url = driver.current_url
        assert Config.AMAZON_URL in current_url, f"URL mismatch! Expected: {Config.AMAZON_URL}, Got: {current_url}"
        logger.info("URL verification passed")

        # Step 4: Perform login actions
        logger.info("Step 4: Starting Amazon login process")
        amazon_page.do_login("gururajking21@gmail.com", "Sharma@1993")
        logger.info("Login process completed")
        
        logger.info("Test completed successfully")
        logger.info("=" * 50)