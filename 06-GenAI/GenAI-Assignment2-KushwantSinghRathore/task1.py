price = float(input("Enter original price: "))

discount_percent = 5
tax_percent = 5

discount_amount = price * (discount_percent / 100)
subtotal = price - discount_amount

tax_amount = subtotal * (tax_percent / 100)

final_total = subtotal + tax_amount

print("\n--- Receipt Breakdown ---")
print("Original Price: ", price)
print("Discount (5%): ", discount_amount)
print("Subtotal after discount: ", subtotal)
print("Tax (5%): ", tax_amount)
print("Final Total Amount: ", final_total)