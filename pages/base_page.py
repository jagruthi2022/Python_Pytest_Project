from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import Logger

class BasePage:
    """Base page class with common methods for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.logger = Logger().get_logger()
    
    def open_url(self, url):
        """Navigate to the specified URL"""
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)
    
    def maximize_window(self):
        """Maximize the browser window"""
        self.logger.info("Maximizing browser window")
        self.driver.maximize_window()
    
    def refresh_page(self):
        """Refresh the current page"""
        self.logger.info("Refreshing page")
        self.driver.refresh()
    
    def find_element(self, locator):
        """Find element with explicit wait"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            self.logger.error(f"Element not found: {locator}")
            raise
    
    def click_element(self, locator):
        """Click on element with explicit wait"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Clicked on element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not clickable: {locator}")
            raise
    
    def enter_text(self, locator, text):
        """Enter text into element"""
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Entered text into element: {locator}")
        except Exception as e:
            self.logger.error(f"Error entering text: {str(e)}")
            raise
    
    def get_title(self):
        """Get page title"""
        return self.driver.title
