# Task 2: Bill Calculator
prices = [120, 350, 'abc', 500, -200, 800]
total = 0

for item in prices:
    try:
        # Check if item is a number by trying to add it
        # This will raise a TypeError if it's a string
        val = item + 0 
        
        if val < 0:
            raise ValueError("Negative price not allowed")
            
        total += val
        print(f"Added {val}, running total is {total}")
        
    except TypeError:
        print(f"Skipping '{item}': Not a number.")
    except ValueError as e:
        print(f"Skipping {item}: {e}")

print(f"Final Total: {total}")