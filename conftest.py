import os
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright

# Resolve repository root: prefer GITHUB_WORKSPACE in CI, otherwise repo root where this file lives
BASE = Path(os.environ.get("GITHUB_WORKSPACE", Path(__file__).resolve().parent))
TEST_RESULTS = BASE / "test-results"

@pytest.fixture(autouse=True)
def ensure_and_log_test_results_dir(request):
    """
    Ensure a test-results directory exists before every test and log its state.
    This helps detect tests/fixtures that remove the directory during the run
    and ensures pytest-html can write the final report.
    """
    # Ensure directory exists before the test runs
    TEST_RESULTS.mkdir(parents=True, exist_ok=True)
    print(f"[conftest] before {request.node.nodeid}: test-results exists={TEST_RESULTS.exists()} -> {TEST_RESULTS}")
    yield
    # Recreate & log after the test (helps detect if a test removed it)
    TEST_RESULTS.mkdir(parents=True, exist_ok=True)
    print(f"[conftest] after  {request.node.nodeid}: test-results exists={TEST_RESULTS.exists()} -> {TEST_RESULTS}")

@pytest.fixture(scope="function")
def page():
    """Provide a Playwright page fixture for tests"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Set to True for headless mode
        page = browser.new_page()
        yield page
        browser.close()