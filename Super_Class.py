class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
        self.you_save=price-deal_price
    
    def display_product_details(self):
       print("Product : {}".format(self.name))
       print("Price : {}".format(self.price))
       print("Deal Price : {}".format(self.deal_price))
       print("You Saved : {}".format(self.you_save))
       print("Ratings : {}".format(self.ratings))
       
p=Product("Laptop",30000,25000,4)
p.display_product_details()