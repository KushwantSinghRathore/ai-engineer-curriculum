order_list = []

while True:
    print("\n--- MENU ---")
    choice = input("1: Add order\n2: Show summary\nq: Quit\nChoose: ")

    if choice == "1":
        amount = input("Enter order amount: ")
        if amount.isdigit():
            order_list.append(int(amount))
            print("Order added!")
        else:
            print("Invalid input.")

    elif choice == "2":
        total_revenue = 0
        discount_count = 0
        print("\n--- Summary Table ---")
        
        for price in order_list:
            if price >= 2000:
                discount = 0.15
            elif price >= 1500:
                discount = 0.10
            elif price >= 1000:
                discount = 0.07
            else:
                discount = 0
            
            final_price = price * (1 - discount)
            total_revenue += final_price
            
            if discount > 0:
                discount_count += 1
            
            print(f"{price} -> {int(discount*100)}% -> {final_price}")
        
        print("Total Revenue:", total_revenue)
        print("Total discounted orders:", discount_count)

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")