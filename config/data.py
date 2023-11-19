import os
from dotenv import load_dotenv

load_dotenv()


class Data:
    
    LOGIN = os.getenv("LOGIN")
    
    @property
    def calc(self):
        return len(self.LOGIN)*5