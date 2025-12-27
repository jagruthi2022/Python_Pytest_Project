import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import Logger
import os

logger = Logger().get_logger()

@pytest.fixture(scope="function")
def driver():
    """Setup and teardown for WebDriver"""
    logger.info("Initializing Chrome WebDriver")
    
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    
    # Initialize driver with error handling
    try:
        # Try with ChromeDriverManager first
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
    except Exception as e:
        logger.error(f"Failed to initialize Chrome WebDriver: {str(e)}")
        raise pytest.UsageError(f"Chrome WebDriver initialization failed: {str(e)}")
    
    yield driver
    
    # Teardown
    logger.info("Closing WebDriver")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            # Get project root directory
            project_root = os.path.dirname(os.path.abspath(__file__))
            screenshot_dir = os.path.join(project_root, "screenshots")
            
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"Test failed. Screenshot saved: {screenshot_path}")
