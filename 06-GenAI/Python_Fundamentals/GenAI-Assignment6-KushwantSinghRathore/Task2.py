prices = [120, 350, 'abc', 500, -200, 800]
total = 0

print("--- Starting Bill Calculation ---\n")

for item in prices:
    try:
        value = item + 0 
        
        if value < 0:
            raise ValueError("Negative price not allowed")
            
        total += value
        print(f"Processed: {value}. Running total: {total}")
        
    except TypeError:
        print(f"Skipping '{item}': Invalid type (not a number).")
    except ValueError as e:
        print(f"Skipping {item}: {e}")

print(f"\n--- Final Bill Total: {total} ---")