class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        return f"Product: {self.name}, Price: ${self.price}, Category: {self.category}"

class ElectronicProduct(Product):
    def __init__(self,name,price,category,warranty_years):
        super().__init__(name,price,category)
        self.warranty_years = warranty_years

    def get_info(self):
        return f"{super().get_info()}, Warranty: {self.warranty_years} years"

laptop = ElectronicProducts("Dell XPS", 1200, "Electronics", 3)
print(laptop.get_info())