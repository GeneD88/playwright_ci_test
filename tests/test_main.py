from base.base_test import SearchFeatureTest
import allure
import pytest

@pytest.mark.usefixtures("screenshot_on_failure")
@allure.feature("Main Feature test")
class TestMainSearchPage(SearchFeatureTest):
    
    @allure.title("Search for Tires")
    def test_search_on_main_page_for(self):
        print(self.data.LOGIN)
        print(self.data.calc)
        self.main_page.open()
        self.main_page.type_in_search("toyo tires")
        self.main_page.click_on_search_button()
        self.search_results_page.check_search_field_value("toyo tires")
        # self.search_results_page.check_search_result_images_displayed()
        self.search_results_page.check_search_results_contain_searched_value("toyo tires")
        # self.main_page.allure_make_screenshot("final_page.png")