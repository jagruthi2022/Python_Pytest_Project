"""
Main entry point to run all test cases
Execute this file to run entire test suite
"""
import pytest
import sys

if __name__ == "__main__":
    # Run all tests with verbose output
    args = [
        "tests/",           # Run all tests in tests folder
        "-v",               # Verbosecd 
        "-s",               # Show print statements
        "--html=reports/report.html",  # Generate HTML report
        "--self-contained-html"
    ]
    
    # Execute pytest with arguments
    exit_code = pytest.main(args)
    
    # Exit with same code as pytest
    sys.exit(exit_code)
