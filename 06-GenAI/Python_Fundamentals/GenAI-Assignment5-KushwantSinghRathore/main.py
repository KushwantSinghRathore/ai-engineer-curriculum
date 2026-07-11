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

from shop_package import apply_discount, calculate_total

# Use of shop package
prices = [100, 200, 300]
total = calculate_total(prices)
final_price = apply_discount(total, 10)

print(f"Total: {total}, Final Price: {final_price}")