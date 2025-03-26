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
        
        
class Order:
    delivery_charges={
        "prime_members": 0,
        "non-prime_members":50
    }
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart=[]
        self.delivery_speed=delivery_speed
        self.delivery_address=delivery_address
        
        
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
        
    def display_order_details(self):
        print("----------Products in Cart---------")
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity : {}".format(quantity))
            print("------------------------------")
            
        print("Delivery speed: {}".format(self.delivery_speed))
        print("Delivery Address: {}".format(self.delivery_address))
        print("Delivery Charges : {}".format(Order.delivery_charges[self.delivery_speed]))
        
        
    def get_delivery_charges(cls):
        return Order.delivery_charges
            
        
        
        
tv=ElectronicItem("TV",40000,30000,3.5,24)
keyboard=ElectronicItem("Logi Tech Keyboard",10000,5000,4.2,12)
mouse=ElectronicItem("Logi Tech mouse",5000,4000,4.2,12)
flour=GroceryItem("Wheat Flour",100,90,4.5,"01/06/2025")
milk=GroceryItem("Amul Milk",40,30,4.5,"10/06/2025")


order=Order("prime_members","Kochi")
order.add_item(milk,3)
order.add_item(tv,1)
order.display_order_details()
print(order.get_delivery_charges())
