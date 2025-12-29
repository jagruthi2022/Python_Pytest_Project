"""
Configuration file for test data and application settings
"""

class Config:
    """Configuration class for application settings"""
    
    # Application URLs
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    AMAZON_URL = "https://www.amazon.in/"
    
    # Browser settings
    BROWSER = "chrome"
    HEADLESS = False
    
    # Timeouts
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    PAGE_LOAD_TIMEOUT = 30
    
    # Test Data
    VALID_USERNAME = "Admin"
    VALID_PASSWORD = "admin123"
    
    # Paths
    SCREENSHOT_PATH = "screenshots/"
    LOG_PATH = "logs/"
    DRIVER_PATH = "drivers/"
