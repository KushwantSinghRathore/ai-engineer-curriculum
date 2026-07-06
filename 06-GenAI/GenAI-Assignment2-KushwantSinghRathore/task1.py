# 1. Grab the raw string
raw_input = input("Enter order amount: ")

# 2. Inspect it using your control flow
if not raw_input.isdigit():
    print("Error: That is not a number! Exiting.")
    exit()

# 3. If the script survived the check above, it is safe to convert!
order_amount = int(raw_input)