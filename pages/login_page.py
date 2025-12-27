"""
Login Page Object - Contains all elements and actions for login page
"""
from selenium.webdriver.common.by import By
from utils.helper import Helper
from utils.logger import Logger

logger = Logger().get_logger()

class LoginPage:
    """Page Object for OrangeHRM Login Page"""
    
    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PROFILE_DROPDOWN = (By.CSS_SELECTOR, "p.oxd-userdropdown-name")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    
    def __init__(self, driver):
        self.driver = driver
        self.helper = Helper()
    
    def open_login_page(self, url):
        """Navigate to login page"""
        logger.info(f"Opening login page: {url}")
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.refresh()
    
    def enter_username(self, username):
        """Enter username"""
        logger.info(f"Entering username: {username}")
        element = self.helper.wait_for_element(self.driver, self.USERNAME_INPUT)
        element.clear()
        element.send_keys(username)
    
    def enter_password(self, password):
        """Enter password"""
        logger.info("Entering password")
        element = self.helper.wait_for_element(self.driver, self.PASSWORD_INPUT)
        element.clear()
        element.send_keys(password)
    
    def click_login_button(self):
        """Click login button"""
        logger.info("Clicking login button")
        element = self.helper.wait_for_element_clickable(self.driver, self.LOGIN_BUTTON)
        element.click()
    
    def do_login(self, username, password):
        """Perform complete login"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        logger.info("Login action completed")
    
    def do_logout(self):
        """Perform logout"""
        logger.info("Waiting 5 seconds before logout")
        self.helper.sleep(5)
        
        logger.info("Clicking profile dropdown")
        element = self.helper.wait_for_element_clickable(self.driver, self.PROFILE_DROPDOWN)
        element.click()
        
        logger.info("Clicking logout button")
        element = self.helper.wait_for_element_clickable(self.driver, self.LOGOUT_BUTTON)
        element.click()
        logger.info("Logout completed")
    
    def is_login_successful(self):
        """Verify login success"""
        try:
            self.helper.wait_for_element(self.driver, self.PROFILE_DROPDOWN)
            logger.info("Login successful - Profile dropdown found")
            return True
        except:
            logger.error("Login failed - Profile dropdown not found")
            return False
