# Playwright Test Suite for Log Analyzer

This directory contains automated end-to-end tests for the Log Analyzer web application using Playwright.

## 📁 Project Structure

```
playwright/
├── pages/                          # Page Object Models
│   ├── home_page.py               # HomePage class
│   ├── upload_page.py             # UploadPage class
│   └── analysis_page.py           # AnalysisPage class
├── tests/                          # Test files
│   ├── test_basic_user_journey.py # Basic homepage and demo tests
│   └── test_demo_page_buttons.py  # Demo page button functionality tests
├── conftest.py                     # Pytest configuration and fixtures
├── pytest.ini                      # Pytest settings
├── requirements.txt                # Python dependencies
├── run_tests.py                    # Simple script to run tests
└── setup.py                        # Setup script for environment
```

## 🚀 Getting Started

### 1. Setup (First Time Only)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

Or simply run:
```bash
python setup.py
```

### 2. Running Tests

#### Option A: Using the run script
```bash
python run_tests.py
```

#### Option B: Using pytest directly
```bash
# Activate virtual environment first
source venv/bin/activate

# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_demo_page_buttons.py -v

# Run specific test
python -m pytest tests/test_demo_page_buttons.py::test_back_to_home_button -v
```

#### Option C: Using PyCharm
1. Right-click on any test file
2. Select "Run 'pytest in test_...'"
3. Or click the green arrow next to individual test functions

## 📝 Test Coverage

### test_basic_user_journey.py
- ✅ `test_homepage_loads` - Verifies homepage loads correctly
- ✅ `test_simple_workflow` - Tests navigation from homepage to demo page

### test_demo_page_buttons.py
- ✅ `test_back_to_home_button` - Tests "Back to Home" button functionality
- ✅ `test_apply_sorting_button` - Tests "Apply Sorting" button works
- ✅ `test_all_sorting_options` - Tests all sorting options (severity, users, occurrences)
- ✅ `test_expand_row_functionality` - Tests clicking rows to expand details
- ✅ `test_all_demo_page_buttons_together` - Comprehensive test of all interactive elements

## 🔧 Configuration

### conftest.py
Contains the `page` fixture that provides a Playwright browser page to all tests:
- Launches Chromium browser (set `headless=False` to see the browser)
- Creates a new page for each test
- Automatically closes the browser after each test

### pytest.ini
Configures pytest behavior:
- Test discovery patterns
- Verbose output
- Short traceback format

## 📊 Test Results

All tests currently pass:
```
7 passed in ~16 seconds
```

## 🎯 Best Practices

1. **Use Page Objects** - Encapsulate page interactions in page object classes
2. **Use Fixtures** - Leverage pytest fixtures for setup/teardown
3. **Descriptive Names** - Use clear, descriptive test function names
4. **Wait Strategies** - Use Playwright's auto-waiting features with `expect()`
5. **Assertions** - Use Playwright's `expect()` for reliable assertions

## 🐛 Debugging

### Run tests with visible browser
Edit `conftest.py` and set `headless=False` (already set by default)

### Take screenshots
```python
page.screenshot(path="debug.png")
```

### Print debug information
```python
print(f"Current URL: {page.url}")
print(f"Page title: {page.title()}")
```

### Run with pytest output
```bash
python -m pytest tests/ -v -s  # -s shows print statements
```

## 📚 Resources

- [Playwright Python Docs](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom)

## 🤝 Contributing

When adding new tests:
1. Create descriptive test names starting with `test_`
2. Use the `page` fixture for browser automation
3. Follow the existing test structure
4. Add docstrings to explain what each test does
5. Run all tests before committing to ensure nothing breaks
