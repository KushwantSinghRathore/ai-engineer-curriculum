# Using 'w' mode to start fresh for this specific task
with open("products.txt", "w") as file:
    for x in range(3):
        print(f"\nEntering details for product {x+1}:")
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        # Writing with correct spacing: "Name | Price"
        file.write(f"{name} | {price}\n")

# Read and print with proper formatting
print("\n--- Product List ---")
with open("products.txt", "r") as file:
    for line in file:
        # strip() removes the newline character at the end for clean printing
        print(line.strip())