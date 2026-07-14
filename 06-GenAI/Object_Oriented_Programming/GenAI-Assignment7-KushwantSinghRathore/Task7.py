# 1. Base Class: Product
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        """Returns string representation for printing."""
        return f"Product: {self.name} | Price: ${self.price} | Category: {self.category}"

    def __add__(self, other):
        """Allows adding the price of two product objects."""
        if isinstance(other, Product):
            return self.price + other.price
        return NotImplemented

# 2. Manager Class: Inventory
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total_value(self):
        """Calculates total price of all items."""
        return sum(p.price for p in self.products)

    def show_all_products(self):
        for p in self.products:
            print(p)

# 3. Interface Class: Store
class Store:
    def __init__(self, name):
        self.store_name = name
        self.inventory = Inventory()

    def add_new_product(self):
        print(f"\n--- Adding to {self.store_name} ---")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        cat = input("Enter product category: ")
        
        # Now Product is defined, so we can create it
        new_prod = Product(name, price, cat)
        self.inventory.add_product(new_prod)
        print("Product added successfully!")

    def show_summary(self):
        print(f"\n--- {self.store_name} Summary ---")
        print(f"Total items: {len(self.inventory.products)}")
        print(f"Total inventory value: ${self.inventory.get_total_value()}")

# 4. Main Execution
if __name__ == "__main__":
    my_store = Store("TechHub")
    
    # Adding 2 products as requested
    my_store.add_new_product()
    my_store.add_new_product()
    
    # Showing summary
    my_store.show_summary()
    
    # Demonstration of __add__
    print("\n--- Operator Overloading Test ---")
    p1 = my_store.inventory.products[0]
    p2 = my_store.inventory.products[1]
    print(f"Combined price of first two items: ${p1 + p2}")