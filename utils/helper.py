"""
Helper utilities for common test operations
"""
import os
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config
from utils.logger import Logger

logger = Logger().get_logger()

class Helper:
    """Helper class with utility methods for tests"""
    
    @staticmethod
    def take_screenshot(driver, test_name):
        """
        Capture screenshot and save with test name
        
        Args:
            driver: WebDriver instance
            test_name: Name of the test for screenshot filename
        """
        if not os.path.exists(Config.SCREENSHOT_PATH):
            os.makedirs(Config.SCREENSHOT_PATH)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{test_name}_{timestamp}.png"
        screenshot_path = os.path.join(Config.SCREENSHOT_PATH, screenshot_name)
        
        driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved: {screenshot_path}")
        return screenshot_path
    
    @staticmethod
    def wait_for_element(driver, locator, timeout=None):
        """
        Wait for element to be present
        
        Args:
            driver: WebDriver instance
            locator: Tuple of (By, value)
            timeout: Wait timeout (default from Config)
        
        Returns:
            WebElement
        """
        if timeout is None:
            timeout = Config.EXPLICIT_WAIT
        
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except Exception as e:
            logger.error(f"Element not found: {locator}, Error: {str(e)}")
            raise
    
    @staticmethod
    def wait_for_element_clickable(driver, locator, timeout=None):
        """
        Wait for element to be clickable
        
        Args:
            driver: WebDriver instance
            locator: Tuple of (By, value)
            timeout: Wait timeout (default from Config)
        
        Returns:
            WebElement
        """
        if timeout is None:
            timeout = Config.EXPLICIT_WAIT
        
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except Exception as e:
            logger.error(f"Element not clickable: {locator}, Error: {str(e)}")
            raise
    
    @staticmethod
    def sleep(seconds):
        """Sleep for specified seconds"""
        logger.info(f"Sleeping for {seconds} seconds")
        time.sleep(seconds)
