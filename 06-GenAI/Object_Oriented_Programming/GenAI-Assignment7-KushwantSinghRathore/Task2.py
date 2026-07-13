class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return  self.__price
        
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Error: Price must be a Positive number")


p1 = Product("Mango", 200, "Fruit")

# Testing the -ve number
p1.set_price(-50)

p1.set_price(250)

print(f"New Price is: {p1.get_price()}")
