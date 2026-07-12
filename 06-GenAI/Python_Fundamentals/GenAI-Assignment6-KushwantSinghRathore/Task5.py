# Task 5: Shopping Cart
cart = []

while True:
    choice = input("Enter price ('q' to quit): ")
    if choice.lower() == 'q':
        break
        
    try:
        price = float(choice)
        if price < 0:
            raise ValueError("Price cannot be negative.")
        cart.append(price)
    except ValueError as e:
        print(f"Invalid input: {e}")

print(f"Total items: {len(cart)}")
print(f"Total bill: {sum(cart)}")