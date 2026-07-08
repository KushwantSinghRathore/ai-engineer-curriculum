calculate_gst = lambda price: price + (price*0.18)

final_price_calc = lambda price, discount: (price * (1 - discount)) * (1.18)

base_price = 100
discount_percent = 0.10

print(f"Base Price: {base_price}")
print(f"Price with 18% GST: {calculate_gst(base_price)}")
print(f"Price with 10% discount and 18% GST: {final_price_calc(base_price, discount_percent)}")