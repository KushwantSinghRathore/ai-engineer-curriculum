prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000,
}

discount = float(input("Enter the discount percentage: "))
total_discounted_sum = 0

with open("discount_report.txt", "w") as file:
    for product, price in prices.items():
        discounted = price * (1 - discount / 100)
        total_discounted_sum += discounted 
        
        file.write(f"{product} | {price} | {discounted:.2f}\n")
    
    # Summary
    avg_price = total_discounted_sum / len(prices)
    file.write(f"\nTotal Items: {len(prices)}\n")
    file.write(f"Average Discounted Price: {avg_price:.2f}\n")

# Reading back the file
print("\n--- Discount Report ---")
with open("discount_report.txt", "r") as f:
    print(f.read())