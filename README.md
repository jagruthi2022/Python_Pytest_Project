"# Python Pytest Selenium Project - OrangeHRM Login Automation

This project automates the login/logout flow for the OrangeHRM demo application using Python, Pytest, and Selenium with the Page Object Model (POM) design pattern.

## Project Structure

```
PYTHON_PYTEST_PROJECT/
├── pages/              # Page Object Model (UI logic)
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
├── tests/              # Test cases only
│   ├── __init__.py
│   └── test_login.py
├── utils/              # Utilities (logging, helpers)
│   ├── __init__.py
│   └── logger.py
├── screenshots/        # Screenshots on test failure
├── logs/               # Execution Logs
│   └── test_execution.log
├── conftest.py         # Pytest fixtures & hooks
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Dependencies
└── README.md
```

## Test Application Details

- **URL**: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- **Username**: Admin
- **Password**: admin123

## Test Steps

1. Open URL
2. Maximize window and refresh
3. Enter username and password
4. Click on submit button
5. Once logged in, sleep 5 seconds then logout

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Chrome browser installed

### Installation

1. Clone or download this project

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test file:
```bash
pytest tests/test_login.py
```

### Run with verbose output:
```bash
pytest -v -s
```

### Run with HTML report:
```bash
pytest --html=reports/report.html
```

## Features

- **Page Object Model (POM)**: Separation of test logic and page elements
- **Logging**: Comprehensive logging for debugging and tracking
- **Screenshot on Failure**: Automatic screenshot capture on test failures
- **HTML Reports**: Pytest HTML reports for test results
- **WebDriver Manager**: Automatic driver management (no manual driver downloads)
- **Reusable Components**: Base page class with common methods

## Project Components

### Pages
- **base_page.py**: Base class with common methods for all page objects
- **login_page.py**: Login page specific methods and locators

### Tests
- **test_login.py**: Test case for login/logout flow

### Utils
- **logger.py**: Custom logger utility for consistent logging

### Configuration
- **conftest.py**: Pytest fixtures and hooks (WebDriver setup, screenshot capture)
- **pytest.ini**: Pytest configuration settings

## Logs and Reports

- Execution logs: `logs/test_execution.log`
- Screenshots: `screenshots/` (captured on test failure)
- HTML reports: `reports/report.html` (after running tests)

## Notes

- Tests use Chrome browser by default
- Implicit wait is set to 10 seconds
- Explicit wait is set to 20 seconds
- Browser window is maximized automatically" 
