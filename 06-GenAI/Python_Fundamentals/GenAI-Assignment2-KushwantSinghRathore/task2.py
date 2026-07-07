# The given list of orders
orders = [1200, 2500, 800, 1750, 3000]

discount_count = 0
total_revenue = 0

for current_order in orders:
    if current_order >= 2000:
        discount_percentage = 0.15
    elif current_order >= 1500 :
        discount_percentage = 0.10
    elif current_order >= 1000 :
        discount_percentage = 0.07
    else:
        discount_percentage = 0
    
    final_amount = current_order * (1 - discount_percentage)
    if discount_percentage > 0:
        discount_count += 1
    total_revenue += final_amount
    print(f"{current_order} -> {discount_percentage*100}% -> {final_amount}")

print(f"Total Revenue after discounts: {total_revenue}")   

print(f"Total orders that received a discount: {discount_count}")