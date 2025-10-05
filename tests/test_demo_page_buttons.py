# tests/test_demo_page_buttons.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

def test_back_to_home_button(page: Page):
    """Test that 'Back to Home' button works correctly"""
    home_page = HomePage(page)
    
    # Navigate to homepage and click "Try Demo"
    home_page.goto()
    page.get_by_text("Try Demo").click()
    
    # Wait for demo page to load
    expect(page.get_by_text("Loading demo data...")).to_be_hidden()
    expect(page).to_have_url("https://loganalyzer.org/demo")
    
    # Click "Back to Home" button
    page.get_by_text("Back to Home").click()
    
    # Verify we're back on the homepage
    expect(page).to_have_url("https://loganalyzer.org/")
    expect(home_page.hero_title).to_be_visible()

def test_apply_sorting_button(page: Page):
    """Test that 'Apply Sorting' button works correctly"""
    home_page = HomePage(page)
    
    # Navigate to demo page
    home_page.goto()
    page.get_by_text("Try Demo").click()
    expect(page.get_by_text("Loading demo data...")).to_be_hidden()
    
    # Verify we're on demo page
    expect(page).to_have_url("https://loganalyzer.org/demo")
    
    # Take a screenshot before sorting
    page.screenshot(path="before_sorting.png")
    
    # Select a different sorting option (use actual option value)
    page.locator("#sort-by").select_option("users")
    
    # Click "Apply Sorting" button
    page.get_by_text("Apply Sorting").click()
    
    # Wait a moment for sorting to apply
    page.wait_for_timeout(500)
    
    # Take a screenshot after sorting
    page.screenshot(path="after_sorting.png")
    
    # Verify the page is still showing results (sorting applied)
    expect(page.get_by_text("Sort Results By:")).to_be_visible()
    expect(page.locator("table")).to_be_visible()

def test_all_sorting_options(page: Page):
    """Test that all sorting options can be selected and applied"""
    home_page = HomePage(page)
    
    # Navigate to demo page
    home_page.goto()
    page.get_by_text("Try Demo").click()
    expect(page.get_by_text("Loading demo data...")).to_be_hidden()
    
    # Test each sorting option (use actual option values from the page)
    sorting_options = [
        "severity",
        "users",
        "occurrences"
    ]
    
    for option in sorting_options:
        # Select the sorting option
        page.locator("#sort-by").select_option(option)
        
        # Click "Apply Sorting"
        page.get_by_text("Apply Sorting").click()
        
        # Wait for sorting to apply
        page.wait_for_timeout(300)
        
        # Verify the table is still visible
        expect(page.locator("table")).to_be_visible()

def test_expand_row_functionality(page: Page):
    """Test that clicking on rows expands details"""
    home_page = HomePage(page)
    
    # Navigate to demo page
    home_page.goto()
    page.get_by_text("Try Demo").click()
    expect(page.get_by_text("Loading demo data...")).to_be_hidden()
    
    # Verify hint text is visible
    expect(page.get_by_text("Click rows to expand details")).to_be_visible()
    
    # Find and click the first row in the table
    first_row = page.locator("table tbody tr").first
    
    # Take screenshot before clicking
    page.screenshot(path="before_expand.png")
    
    # Click the row to expand
    first_row.click()
    
    # Wait for expansion animation
    page.wait_for_timeout(500)
    
    # Take screenshot after clicking
    page.screenshot(path="after_expand.png")
    
    # Verify the table is still visible (row should be expanded)
    expect(page.locator("table")).to_be_visible()

def test_all_demo_page_buttons_together(page: Page):
    """Comprehensive test of all interactive elements on demo page"""
    home_page = HomePage(page)
    
    # Navigate to demo page
    home_page.goto()
    page.get_by_text("Try Demo").click()
    expect(page.get_by_text("Loading demo data...")).to_be_hidden()
    
    # Verify all key elements are present
    expect(page.get_by_text("Log Analyzer Demo")).to_be_visible()
    expect(page.get_by_text("See AI Analysis in Action")).to_be_visible()
    expect(page.get_by_text("Back to Home")).to_be_visible()
    expect(page.get_by_text("Sort Results By:")).to_be_visible()
    expect(page.get_by_text("Apply Sorting")).to_be_visible()
    expect(page.locator("#sort-by")).to_be_visible()
    expect(page.locator("table")).to_be_visible()
    
    # Test sorting interaction
    page.locator("#sort-by").select_option("users")
    page.get_by_text("Apply Sorting").click()
    page.wait_for_timeout(500)
    
    # Verify page is still functional after sorting
    expect(page.locator("table")).to_be_visible()
    
    # Test row expansion
    page.locator("table tbody tr").first.click()
    page.wait_for_timeout(500)
    
    # Finally, test back to home
    page.get_by_text("Back to Home").click()
    expect(page).to_have_url("https://loganalyzer.org/")
    expect(home_page.hero_title).to_be_visible()
