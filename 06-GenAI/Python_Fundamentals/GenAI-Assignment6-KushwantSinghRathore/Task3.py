def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    else:
        print(f"Age {age} is valid.")

# Main Code
try:
    user_input = int(input("Enter your age: "))
    check_age(user_input)
    
except ValueError as e:
    print(f"Error: {e}")