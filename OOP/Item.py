class Item:
    def __init__(self,name:str,price:int,quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Python doesn't support constructor overloading
    # def __init__(self,name, price, special,color,quantity):
    #     self.name = name
    #     self.price = price
    #     self.special = special
    #     self.color = color
    #     self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    # def discount (self):
    #     if self.color == "Red":
    #         return '50 percent discount'
    #     elif self.color == "Yellow":
    #         return '30 percent discount'


# First object
item1 = Item("Laptop",300,5)
print(item1.calculate_total_price())
# Second object
item2 = Item("Mobile",500,5)
print(item2.calculate_total_price())
# third object
# item3 = Item("Iphone",500,True,"Yellow",500)
# print(item3.calculate_total_price())
# print(item3.discount())