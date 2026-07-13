class Product:
    def __init__(self, name, price,category):
        self.name = name
        self.price = price

class Laptop(Product):
    def get_info(self):
        return f"LAPTOP INFO: {self.name} is a powerful computer, price is ${self.price}."

class Mobile(Product):
    def get_info(self):
        return f"MOBILE INFO: {self.name} is a handheld device, price is ${self.price}."

gadgets = [
    Laptop("Dell XPS", 1200, "Electronics"),
    Mobile("iPhone 15", 999, "Electronics")
]

for item in gadgets:
    print(item.get_info())