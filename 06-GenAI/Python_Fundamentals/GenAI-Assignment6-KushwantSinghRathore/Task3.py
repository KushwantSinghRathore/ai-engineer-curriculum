# Task 3: Age Validator
def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    print(f"Age {age} is valid.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as e:
    print(f"Error: {e}")