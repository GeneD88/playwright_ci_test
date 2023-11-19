from base.base_page import InitPage
from config.urls import Urls
import allure
import time

class MainPage(InitPage):
    
    PAGE_URL = Urls.MAIN

    
    search_input_field = "//input[@aria-label='Запрос']"
    search_button = "//button[@type='submit']"
    currency_info = "//div[@aria-label='Биржевые курсы']"
    
    def type_in_search(self, search_value):
        with allure.step(f"Type in {search_value}"):
            print(dir(self))
            self.page.locator(self.search_input_field).fill(search_value) #.type(search_value, timeout = 2000, delay = 100)
        
        
    @allure.step("Check if search button is visible")
    @property
    def is_search_button_visible_and_clickable(self) -> bool:
        return self.page.locator(self.search_button).is_visible()
        
    @allure.step("Click on Search Button")
    def click_on_search_button(self):
        self.page.locator(self.search_button).click()
        

        