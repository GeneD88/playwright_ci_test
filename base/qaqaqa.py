
def num():
    return 4

class First:
    def __init__(self):
        self.num = 8
        
        
class Second(First):
    
    def calc(self):
        return self.num * 2
    
b = Second()

print(b.calc())


