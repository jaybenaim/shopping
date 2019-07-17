import product 

class Cart:
    ''' 
    This will represent a users shopping cart filled with products 
    ''' 

    def __init__(self, products, total_price): 
        self.products = [] 
        self.total_price = total_price 

    def add_product(self, product_to_add): 
        self.products.append(product_to_add)  
        # adds instance of product ? 


    def remove_product(self, product_to_remove, price): 
        self.products.pop(self.products.index(product_to_remove))
        self.total_price -= price 

    
    def total_cost(self, tax_rate): 
        # self.total_price += 
        tax = tax_rate / 10
        # if self.total_price == float: 
        #     return round(self.total_price, 2)
        # elif self.total_price != float: 
        #     return float(self.total_price) 
        if self.total_price <= 0: 
            return self.total 
        else: 
            return f'''
        Your Shopping Cart: {self.products}
      -------------------------------------------------
           | The price before tax is ${float(round(self.total_price, 2))}0 |
           --------------------------------
           | The price after tax is ${round((self.total_price + tax), 2) }0 |
           --------------------------------
        ''' 

    def highest_priced_item(self): 
        for item in self.products: ## look in items 
            # get the total cost for each product
            
            # get max from list of totals
            highest = max(self.products)
        return highest 

soap = product.Product('soap', 10, 13)
carted = Cart('soap', soap.base_price)

carted.add_product('soap') 
carted.add_product('eggs') 
carted.add_product('apple') 
print(carted.total_cost(13)) 
# print(carted.highest_priced_item()) # print highest priced item 
carted.remove_product('soap', soap.get_total()) # remove soap item 
# print(carted.total_cost(13))
# print(carted.products) # see all the products in cart 
