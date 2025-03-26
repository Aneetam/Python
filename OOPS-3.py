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
        
class ElectronicItem(Product):
    def __init__(self,name,price,deal_price,rating,warranty_in_months):
        super().__init__(name,price,deal_price,rating)
        self.warranty_in_months=warranty_in_months
        
    def get_warranty_in_months(self):
        return self.warranty_in_months
        
    def display_product_details(self):
        super().display_product_details()
        print("Warranty: {}".format(self.warranty_in_months))
        

class GroceryItem(Product):
    def __init__(self,name,price,deal_price,rating,expiry_date):
        super().__init__(name,price,deal_price,rating)
        self.expiry_date=expiry_date
        
    def display_product_details(self):
        super().display_product_details()
        print("Expiray Date: {}".format(self.expiry_date))
            
        
        
        


flour=GroceryItem("Wheat Flour",100,90,4.5,"01/06/2025")
flour.display_product_details()