class Product(): 
    ''' This represents a product a user can add to their cart ''' 

    def __init__(self,name, base_price, tax_rate): 
        self.name = name 
        self.base_price = base_price 
        self.tax_rate = tax_rate 

    def get_total(self): 
        total = 0 
        tax = self.tax_rate / 10 
        total += self.base_price + tax 
        return total 

