class Cart:
   flat_discount = 0
   min_bill = 100
   def __init__(self):
       self.items = {}
   def add_item(self, item_name,quantity):
       self.items[item_name] = quantity
   def display_items(self):
       print(self.items)
print(Cart.items)