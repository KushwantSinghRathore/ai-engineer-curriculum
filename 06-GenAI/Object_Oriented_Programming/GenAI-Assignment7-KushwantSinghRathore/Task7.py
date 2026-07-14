# Base Product class
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product: {self.name} | Price: ${self.price} | Category: {self.category}"

    def __add__(self, other):
        return self.price + other.price

# Inventory Manager
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                print(f"Successfully removed: {name}")
                return
        print(f"Product '{name}' not found.")

    def get_total_value(self):
        total = 0
        for p in self.products:
            total += p.price
        return total

# Store Interface
class Store:
    def __init__(self, name):
        self.store_name = name
        self.inventory = Inventory()


# Create Store
my_store = Store("Tech Shop")

# Create 3 products
p1 = Product("Laptop", 1000, "Electronics")
p2 = Product("Mouse", 20, "Electronics")
p3 = Product("Keyboard", 50, "Electronics")

# Add 3 products
my_store.inventory.add_product(p1)
my_store.inventory.add_product(p2)
my_store.inventory.add_product(p3)

# Demonstrate removal
my_store.inventory.remove_product("Mouse")

# Show Summary
print(f"Total items in inventory: {len(my_store.inventory.products)}")
print(f"Total value of inventory: ${my_store.inventory.get_total_value()}")

# Use __add__ to combine prices of two products
combined_price = p1 + p3
print(f"Combined price of Laptop and Keyboard: ${combined_price}")