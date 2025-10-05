from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.upload_button = page.locator('[data-testid="upload-btn"]')
        self.hero_title = page.locator('h1')
        self.features_section = page.locator('[data-testid="features"]')
    
    def goto(self):
        self.page.goto('https://loganalyzer.org/')
    
    def click_upload(self):
        self.upload_button.click()

