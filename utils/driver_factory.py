"""
Driver Factory - Creates and configures WebDriver instances
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config
from utils.logger import Logger

logger = Logger().get_logger()

class DriverFactory:
    """Factory class for creating WebDriver instances"""
    
    @staticmethod
    def get_driver(browser=None):
        """
        Create and return WebDriver instance based on browser type
        
        Args:
            browser: Browser type (chrome, firefox, edge). Default from Config
        
        Returns:
            WebDriver instance
        """
        if browser is None:
            browser = Config.BROWSER.lower()
        
        driver = None
        
        if browser == "chrome":
            logger.info("Initializing Chrome driver")
            chrome_options = webdriver.ChromeOptions()
            
            if Config.HEADLESS:
                chrome_options.add_argument("--headless")
            
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-popup-blocking")
            
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=chrome_options
            )
        
        elif browser == "firefox":
            logger.info("Initializing Firefox driver")
            driver = webdriver.Firefox()
        
        elif browser == "edge":
            logger.info("Initializing Edge driver")
            driver = webdriver.Edge()
        
        else:
            logger.error(f"Unsupported browser: {browser}")
            raise ValueError(f"Browser '{browser}' is not supported")
        
        # Set timeouts
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        logger.info(f"{browser.capitalize()} driver initialized successfully")
        return driver
    
    @staticmethod
    def quit_driver(driver):
        """Close and quit the WebDriver instance"""
        if driver:
            logger.info("Closing driver")
            driver.quit()
