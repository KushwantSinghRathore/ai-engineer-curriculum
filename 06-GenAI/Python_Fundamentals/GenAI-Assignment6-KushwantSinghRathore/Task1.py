try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: 0 cannot be used as a denominator.")
else:
    # Print the result only if no errors occurred
    print(f"The result is: {result}")
finally:
    print("Operation Complete")