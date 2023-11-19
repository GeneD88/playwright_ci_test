from base.base_page import BasePage

class CurrencyPage(BasePage):
    
    CURRENCY_PAGE = "https://ya.ru/search/?lr=192&text=USD+MOEX&wiz=finance"
    
    progress_spinner = "div[class*='progress'"
    
    
    
    def verify_spinner_is_visible(self):
        assert self.page.locator(self.progress_spinner).is_visible()