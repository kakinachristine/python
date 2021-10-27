import module2
class product(object):
    def __int__(self, name, price, quantity):
        self.ProductName = name
        self.ProductPrice = price
        self.ProductQuantity= quantity
product1 = product("sugar","200","3kg")
product2 = product("rice", "300", "2kg")
product3 = product("maize flour", "100", "2kg")
product4 = product("wheat flour", "150", "1kg")

     def discount(price):
    """20% discount allowed on all products"""
    discount = (price *20)/100
    print("your new price after discount will be", discount)
class service(product):
    def provider(self):
        product4 = product("goods", "150", "1kg")



