from playwright.sync_api import Page, expect

class UploadPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_input = page.locator('input[type="file"]')
        self.upload_area = page.locator('[data-testid="upload-area"]')
        self.progress_bar = page.locator('[data-testid="progress"]')
    
    def upload_file(self, file_path: str):
        self.file_input.set_input_files(file_path)
    
    def drag_and_drop_file(self, file_path: str):
        # Simulate drag and drop
        self.upload_area.set_input_files(file_path)
    
    def wait_for_upload_complete(self):
        expect(self.progress_bar).to_have_attribute('data-complete', 'true')