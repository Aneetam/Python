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
       
       
class ElectronicItem(Product):
    def set_warranty(self,warranty_in_months):
        self.warranty_in_months=warranty_in_months
    def get_warranty(self):
            return self.warranty_in_months
    def display_product_details(self):
        super().display_product_details()
        print("Warranty : {}".format(self.warranty_in_months))
        
        
class GroceryItem(Product):
    def set_expiry_date(self,exprity_date):
        self.exprity_date=exprity_date
    def get_expiry_date(self):
        return self.exprity_date
        
        
class Order:
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart=[]
        self.delivery_speed=delivery_speed
        self.delivery_address=delivery_address
        
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
        
    def display_order_details(self):
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity : {}".format(quantity))
            
    def display_total_bill(self):
        total_bill=0
        for product,quantity in self.items_in_cart:
            price=product.deal_price * quantity
            total_bill+=price
        print("Total Price : {}".format(total_bill))
        
       

tv=ElectronicItem("TV",450000,40000,4)
tv.set_warranty(24)
tv.display_product_details()