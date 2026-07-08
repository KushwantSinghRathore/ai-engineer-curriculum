price = [100, 250, 400, 1200, 50]

final_price = list(map(lambda price: price + (price*0.18) , price))

print(f"The Orignal price is: {price}")
print(f"The price after GST is: {final_price}")