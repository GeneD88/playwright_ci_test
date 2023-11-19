from playwright.sync_api import Page
import allure
from allure_commons.types import AttachmentType

# class BasePage:
    
#     def ___init___(self, page: Page):
#         # super().__init__(page)
#         self.page = page
#         self.pisya = "piska"
        
#         # self.PAGE_URL = "https://ya.ru"
        
#         self.open()
        
#     # @abstractmethod
#     def open(self):
#         with allure.step(f"Open {self.PAGE_URL}"):
#             self.page.goto(self.PAGE_URL)
#             time.sleep(5)
        
#     # @property
#     # def is_opened(self):
#     #     return self.page.url  == self.PAGE_URL
    
#     # def make_screenshot(self, file_name):
# allure.attach(
#             self.page.screenshot(),
#             file_name,
#             AttachmentType.PNG
#         )


class InitPage:
    
    def __init__(self, page: Page):
        self.page = page
        # self.open()
        
  
    def open(self):
        if self.PAGE_URL:
            with allure.step(f"Open {self.PAGE_URL}"):
                self.page.goto(self.PAGE_URL)
        
        
    @property
    def is_opened(self):
        return self.page.url  == self.PAGE_URL
    
    def allure_make_screenshot(self, file_name):
        allure.attach(
                    self.page.screenshot(),
                    file_name,
                    AttachmentType.PNG
                )