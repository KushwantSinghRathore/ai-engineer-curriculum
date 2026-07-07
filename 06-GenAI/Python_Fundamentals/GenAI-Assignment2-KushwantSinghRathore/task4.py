daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0
for sale in daily:
    if sale <= -1:
        print("Corrupted data! Stopping...")
        break
    elif sale == 0:
        print("No sales today, skipping.")
        continue
    else:
        total_sales += sale
        print(f"Running total: {total_sales}")
print(f"The total sale is: {total_sales}")        