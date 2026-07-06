# 1. Initialize storage outside the loop
order_list = []

# 2. Start the menu engine
while True:
    print("\n--- MENU ---")
    menu = input("1: Add order\n2: Show summary\nq: Quit\nChoose: ")

    # 3. Add to the running list
    if menu == "1":
        amount_str = input("Enter order amount: ")
        if amount_str.isdigit():
            order_list.append(int(amount_str))
            print("Order added!")
        else:
            print("Invalid input! Please enter a number.")
            continue

    # 4. Process all orders (The Task 2 logic)
    elif menu == "2":
        total_revenue = 0
        discount_count = 0
        print("\n--- Summary Table ---")
        
        # This loop processes the "running list"
        for current_order in order_list:
            if current_order >= 2000:
                discount_percentage = 0.15
            elif current_order >= 1500:
                discount_percentage = 0.10
            elif current_order >= 1000:
                discount_percentage = 0.07
            else:
                discount_percentage = 0
            
            final_amount = current_order * (1 - discount_percentage)
            total_revenue += final_amount
            if discount_percentage > 0:
                discount_count += 1
            print(f"{current_order} -> {discount_percentage*100}% -> {final_amount}")
        
        print(f"Total Revenue: {total_revenue}")
        print(f"Total discounted orders: {discount_count}")

    # 5. Quit
    elif menu == "q" or menu == "Q":
        print("Goodbye!")
        break

    # 6. Handle invalid input
    else:
        print("Invalid choice, please try again.")
        continue