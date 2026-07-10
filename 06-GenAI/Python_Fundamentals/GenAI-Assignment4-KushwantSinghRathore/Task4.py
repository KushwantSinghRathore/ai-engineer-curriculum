with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    sales_list = [int(line.strip()) for line in lines]
    
    # Calculate statistics
    total_sale = sum(sales_list)
    highest_sale = max(sales_list)
    lowest_sale = min(sales_list)
    average_sale = total_sale / len(sales_list)
    
    # Print clean summary report
    print("--- Sales Summary Report ---")
    print(f"Total Sales:   {total_sale}")
    print(f"Highest Sale:  {highest_sale}")
    print(f"Lowest Sale:   {lowest_sale}")
    print(f"Average Sale:  {average_sale:.2f}") 