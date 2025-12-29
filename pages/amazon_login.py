"""
Amazon Login Page Object - Contains all elements and actions for Amazon page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class AmazonLoginPage(BasePage):
    """Page Object for Amazon Login Page"""
    
    # Locators
    #ACCOUNT_LISTS = (By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']")
    ACCOUNT_LISTS = (By.XPATH, "//*[@id='nav-link-accountList']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#nav-flyout-ya-signin a")
    #SIGN_IN_BUTTON = (By.XPATH, "//*[@button='Sign in']")
    #EMAIL_INPUT = (By.ID, "ap_email")
    EMAIL_INPUT = (By.XPATH, "//*[@id='ap_email_login']")

    #CONTINUE_BUTTON = (By.ID, "continue")
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='continue']")
    #PASSWORD_INPUT = (By.ID, "ap_password")
    PASSWORD_INPUT = (By.XPATH, "//*[@name='password']")

    #SIGN_IN_SUBMIT = (By.ID, "signInSubmit")
    SIGN_IN_SUBMIT = (By.XPATH, "//*[@id='signInSubmit']")
    #SEARCH_BOX = (By.XPATH, "//*[@id='twotabsearchtextbox']")
    SEARCH_BOX = (By.XPATH, "//*[@id='twotabsearchtextbox']")
    
    def __init__(self, driver):
        """Initialize the AmazonLoginPage with driver and inherit from BasePage"""
        super().__init__(driver)
        self.explicit_wait = WebDriverWait(driver, 20)
    
    def open_amazon_page(self, url):
        """Navigate to Amazon page"""
        self.logger.info(f"Opening Amazon page: {url}")
        self.open_url(url)
        self.maximize_window()
        self.refresh_page()
        time.sleep(10)    # Wait for page to load
        self.logger.info("Amazon page opened and window maximized")
    
    def hover_and_click_sign_in(self):
        """Hover over Account & Lists and click Sign in"""
        self.logger.info("Hovering over Account & Lists")
        account_element = self.explicit_wait.until(EC.presence_of_element_located(self.ACCOUNT_LISTS))
        self.hover_over_element(self.ACCOUNT_LISTS)
        time.sleep(2)  # Wait for dropdown to appear
        
        self.logger.info("Clicking Sign in button")
        sign_in_btn = self.explicit_wait.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON))
        sign_in_btn.click()
        self.logger.info("Sign in button clicked")
    
    def enter_email(self, email):
        """Enter email address"""
        self.logger.info(f"Entering email: {email}")
        try:
            # Wait longer and try multiple locators
            time.sleep(3)  # Wait for page transition
            email_input = self.explicit_wait.until(EC.presence_of_element_located(self.EMAIL_INPUT))
            email_input.clear()
            email_input.send_keys(email)
            self.logger.info("Email entered successfully")
        except Exception as e:
            self.logger.error(f"Failed to enter email: {str(e)}")
            # Try alternative approach
            email_input = self.driver.find_element(By.NAME, "email")
            email_input.clear()
            email_input.send_keys(email)
    
    def click_continue(self):
        """Click continue button"""
        self.logger.info("Clicking continue button")
        continue_btn = self.explicit_wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        continue_btn.click()
    
    def enter_password(self, password):
        """Enter password"""
        self.logger.info("Entering password")
        password_input = self.explicit_wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)
    
    def click_sign_in_submit(self):
        """Click sign in submit button"""
        self.logger.info("Clicking sign in submit button")
        submit_btn = self.explicit_wait.until(EC.element_to_be_clickable(self.SIGN_IN_SUBMIT))
        submit_btn.click()
    
    def do_login(self, email, password):
        """Perform complete Amazon login"""
        self.hover_and_click_sign_in()
        self.enter_email(email)
        self.click_continue()
        self.enter_password(password)
        self.click_sign_in_submit()
        self.logger.info("Amazon login action completed")

    def search_item(self, item):
        """"search for product"""
        self.logger.info("we are searching the product")    
        search_input = self.explicit_wait.until(EC.presence_of_element_located(self.SEARCH_BOX))
        search_input.clear()
        search_input.send_keys(item)
        self.logger.info(f"searched for {item} successfully")
        search_box = self.explicit_wait.until(EC.presence_of_element_located(self.SEARCH_BOX))
        search_box.submit()
        AmazonLoginPage.sleep(self, 10)

            

