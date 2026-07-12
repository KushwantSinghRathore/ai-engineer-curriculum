# Task 1: Safe Division
try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
except ValueError:
    print("Error: Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Operation Complete")