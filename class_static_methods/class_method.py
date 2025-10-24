class Book:
    tax_rate  = 0.07 #7% Mehrwertsteuer

    def __init__(self,title:str,price:float):
        self.title = title
        self.price =price

    def final_price(self)->float:
        return self.price * (1 + Book.tax_rate)
    

    @classmethod
    def set_tax_rate(cls,rate:float):
        cls.tax_rate = rate

    # def change_tax_rate(self, rate: float): # nicht zu empfehelen!
    #     Book.tax_rate = rate
    @staticmethod
    def set_tax_rate_static(rate:float):
        Book.tax_rate = rate

###### Test

b1 = Book("Python 1",30.0)
b2 = Book("Python 1",30.0)
print(b1.final_price())
#Book.set_tax_rate(0.19)
#b1.change_tax_rate(0.19)
Book.set_tax_rate_static(0.19)
print(b1.final_price())
print(b2.final_price())