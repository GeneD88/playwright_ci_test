from base.base_page import InitPage
import allure
from config.urls import Urls
from termcolor import colored
import time

class SearchResultPage(InitPage):
    
    PAGE_URL = "https://google.com"
    
    
    search_field = "//form[@aria-label='Поиск в интернете']/div/input"
    
    search_results_images_scroller = "//div[@role='list' and @class='Scroller-Wrap']/div/a"
    
    search_results = "//ul[@id='search-result']/li[@data-cid]//span[contains(@class, 'organic__title')]"
    
    
    @allure.step("Clear input field")
    def clear_search_input(self):
        self.page.locator(self.search_field).clear()
    
    def check_search_field_value(self, value):
        with allure.step(f"Check input field value {value}"):
            visible_value = self.page.locator(self.search_field).input_value()
            print(colored(f"Visible value: {visible_value}", "green"))
            assert  visible_value == value
        
    @allure.step("Check returned results have images on top")
    def check_search_result_images_displayed(self):
        assert all([x.is_visible() for x in self.page.locator(self.search_results_images_scroller).all()])
        
    def check_search_results_contain_searched_value(self, value, timeout = 5):
        if timeout:
            time.sleep(timeout)
        with allure.step(f"Verify returned results contain searched value: {value}"):
            all_elements = self.page.locator(self.search_results).all()
            if all_elements:
                print(colored(len(all_elements), "green"))
                for el in all_elements:
                    print(colored(el.inner_text(), "light_grey"))
                assert any([value.lower() in x.inner_text().lower() for x in all_elements])
            else:
                raise Exception("Check it out! There are no results but it should have.")
        