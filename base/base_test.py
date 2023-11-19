from pages.main_page import MainPage
from pages.search_results_page import SearchResultPage
import pytest
from playwright.sync_api import Page
from config.data import Data

class SearchFeatureTest:
    
    data: Data
    
    main_page: MainPage
    search_results_page: SearchResultPage
    
    
    @pytest.fixture(autouse=True)
    def setup(self, request, page: Page):
        request.cls.page = page
        request.cls.data = Data()
        request.cls.main_page = MainPage(page)
        request.cls.search_results_page = SearchResultPage(page)