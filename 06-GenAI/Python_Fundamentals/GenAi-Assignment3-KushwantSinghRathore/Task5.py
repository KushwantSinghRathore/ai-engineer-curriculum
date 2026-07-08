prices = [100, 250, 400, 1200, 50, 2000, 850]

greater_num = list(filter(lambda x : x > 500,prices))
less_num = list(filter(lambda x : x <= 500,prices))

print(f" Greater numbers are: {greater_num}")
print(f"Less number are: {less_num}")