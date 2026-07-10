new_data = [5000,2500,1700]

# Append new sales
with open("sales_data.txt" , "a") as f:
    for data in new_data:
        f.write(str(data) + "\n")

# Reopen and print updated file
print("--- Updated File Content ---")
with open("sales_data.txt", "r") as file:
    content = file.read()
    print(content)

with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    print("--- Updated File Content ---")
    print("".join(lines)) # Join the list back into a string to print it
    print(f"Total number of lines: {len(lines)}")