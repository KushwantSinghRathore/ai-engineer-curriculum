cart = []

print("--- Safe Shopping Cart ---")
print("Enter item prices (type 'q' to quit)")

while True:
    user_input = input("Enter price: ")
    
    # Check for exit
    if user_input.lower() == 'q':
        break
        
    try:
        # Convert to float
        price = float(user_input)
        
        # Raise custom exception for negative price
        if price < 0:
            raise ValueError("Price cannot be negative.")
            
        # If everything is valid, add to cart
        cart.append(price)
        print(f"Added ${price:.2f}")
        
    except ValueError as e:
        # Catches both non-numeric input and our custom negative price error
        print(f"Error: {e} Please enter a valid positive number.")

# Summary
print("\n--- Receipt ---")
print(f"Total items: {len(cart)}")
print(f"Total bill: ${sum(cart):.2f}")