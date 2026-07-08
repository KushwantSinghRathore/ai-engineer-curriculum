def process_prices(prices):

    discounted_prices = list(map(lambda x : x * 0.9, prices))
    filtered_prices = list(filter(lambda x : x > 300, discounted_prices))
    return discounted_prices,filtered_prices

test_list = [100, 500, 900, 50, 750]
all_discounted, filtered = process_prices(test_list)

print(f"Original prices: {test_list}")
print(f"Discounted prices: {all_discounted}")
print(f"Filtered prices (> 300): {filtered}")