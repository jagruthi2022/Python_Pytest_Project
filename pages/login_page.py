"""
Login Page Object - Contains all elements and actions for login page
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    """Page Object for OrangeHRM Login Page"""
    
    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PROFILE_DROPDOWN = (By.CSS_SELECTOR, "p.oxd-userdropdown-name")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    
    def __init__(self, driver):
        """Initialize the LoginPage with driver and inherit from BasePage"""
        super().__init__(driver)
    
    def open_login_page(self, url):
        """Navigate to login page"""
        self.open_url(url)
        self.maximize_window()
        self.refresh_page()
    
    def enter_username(self, username):
        """Enter username"""
        self.logger.info(f"Entering username: {username}")
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """Enter password"""
        self.logger.info("Entering password")
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Click login button"""
        self.logger.info("Clicking login button")
        self.click_element(self.LOGIN_BUTTON)
    
    def do_login(self, username, password):
        """Perform complete login"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.logger.info("Login action completed")
    
    def do_logout(self):
        """Perform logout"""
        self.logger.info("Waiting 5 seconds before logout")
        time.sleep(5)
        
        self.logger.info("Clicking profile dropdown")
        self.click_element(self.PROFILE_DROPDOWN)
        
        self.logger.info("Clicking logout button")
        self.click_element(self.LOGOUT_BUTTON)
        self.logger.info("Logout completed")
    
    def is_login_successful(self):
        """Verify login success"""
        try:
            self.find_element(self.PROFILE_DROPDOWN)
            self.logger.info("Login successful - Profile dropdown found")
            return True
        except:
            self.logger.error("Login failed - Profile dropdown not found")
            return False
