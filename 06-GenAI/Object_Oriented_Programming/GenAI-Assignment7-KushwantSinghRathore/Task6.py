class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        """Returns a human-readable string representation of the product."""
        return f"Product(name='{self.name}', price={self.price}, category='{self.category}')"

    def __add__(self, other):
        """Allows adding two product prices together using the '+' operator."""
        if isinstance(other, Product):
            return self.price + other.price
        return NotImplemented

# --- Testing ---
p1 = Product("Laptop", 1000, "Electronics")
p2 = Product("Mouse", 50, "Electronics")

print(p1)  # Automatically calls __str__
print(f"Total price of both: ${p1 + p2}") # Automatically calls __add__