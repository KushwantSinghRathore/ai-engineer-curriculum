class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Product: {self.name}, Price: ${self.price}, Category: {self.category}")

    # Adding the optional discount method
    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        return self.price - discount_amount

# Creating two objects as requested
p1 = Product("Mango", 200, "Fruit")
p2 = Product("Laptop", 50000, "Electronics")

# Calling get_info() for both
p1.get_info()
p2.get_info()

# Demonstration of the optional discount method
print(f"Discounted price for {p1.name}: ${p1.apply_discount(10)}")