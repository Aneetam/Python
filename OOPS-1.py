class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating
        self.you_save=price-deal_price
        
    def display_product_details(self):
        print("Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("You Save: {}".format(self.you_save))
        print("Rating: {}".format(self.rating))
        
    def get_deal_price(self):
        return self.deal_price
        
        
tv=Product("TV",40000,30000,3.5)
tv.display_product_details()
print(tv.deal_price)
print(tv.get_deal_price())