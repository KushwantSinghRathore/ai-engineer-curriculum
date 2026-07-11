import math_utils as mu
from math_utils import square

a = int(input("Enter value 1: "))
b = int(input("Enter value 2: "))

n = int(input("Enter value for square: "))
print(f"Addition is: {mu.add(a,b)}")
print(f"Subtraction is: {mu.subtract(a,b)}")
print(f"Square is: {square(n)}")


# using string_utils.py
import string_utils

# Test data
my_text = "hello python world"

# Calling module functions
print("Capitalized:", string_utils.capitalize_words(my_text))
print("Reversed:", string_utils.reverse_string(my_text))
print("Word count:", string_utils.word_count(my_text))

# Importing the Package
import shop_package.discount as disc
from shop_package.billing import calculate_total

# Testing the package functions
print(f"Discounted Price: {disc.apply_discount(1000, 10)}")
print(f"Total Bill: {calculate_total([100, 200, 300])}")