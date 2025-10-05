# tests/test_homepage.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.upload_page import UploadPage  
from pages.analysis_page import AnalysisPage

def test_homepage_loads(page: Page):
    """Test that homepage loads correctly"""
    home_page = HomePage(page)
    home_page.goto()
    expect(home_page.hero_title).to_be_visible()

def test_simple_workflow(page: Page):
    """Simple test to verify basic functionality"""
    home_page = HomePage(page)
    
    # Navigate to site
    home_page.goto()
    expect(home_page.hero_title).to_be_visible()
    
    # Click "Try Demo"
    page.get_by_text("Try Demo").click()

    # Wait for demo to load
    expect(page.get_by_text("Loading demo data...")).to_be_hidden()
    
    # Verify we're on the demo page
    expect(page).to_have_url("https://loganalyzer.org/demo")
    
    # Check that demo results are visible
    expect(page.get_by_text("See AI Analysis in Action")).to_be_visible()
    expect(page.get_by_text("Sort Results By:")).to_be_visible()
    
    # Verify the "Apply Sorting" button is visible
    expect(page.get_by_text("Apply Sorting")).to_be_visible()