def add_price(prices_list,prices):
    prices_list.append(prices)

def get_average_price(prices_list):
    if len(prices_list) == 0:
         return 0
    else:
        return sum(prices_list) / len(prices_list)
def get_max_price(prices_list):
    if len(prices_list) == 0: return 0
    else:
        return max(prices_list)
prices = []
while True:
    print("\n--- Menu ---")
    print("1 -> Add price")
    print("2 -> Show average price")
    print("3 -> Show highest price")
    print("q -> Quit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        # Get the price from user and convert to float
        new_price = float(input("Enter the price: "))
        add_price(prices, new_price) 
        print("Price added!")
        
    elif choice == '2':
        avg = get_average_price(prices)
        print(f"Average Price: {avg}")
        
    elif choice == '3':
        highest = get_max_price(prices)
        print(f"Highest Price: {highest}")
        
    elif choice == 'q':
        print("Exiting...")
        break