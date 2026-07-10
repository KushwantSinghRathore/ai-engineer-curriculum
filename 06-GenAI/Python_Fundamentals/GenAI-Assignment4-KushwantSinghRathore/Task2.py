# for real full file

with open("sales_data.txt", "r") as file:
    print(file.read())


with open("sales_data.txt", "r") as file:
    first_line = file.readline()
    print(first_line)

with open("sales_data.txt", "r") as file:
    lines = file.readlines()

    sales_list = [int(line.strip())for line in lines]
    print("--- List of Integers ---")
    print(sales_list)
    print(f"Type check: {type(sales_list[0])}") # Verifying it's an integer