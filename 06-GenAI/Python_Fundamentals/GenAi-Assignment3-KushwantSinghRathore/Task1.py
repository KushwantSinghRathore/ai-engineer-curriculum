def apply_discount(price, discount_percent=5):
    
    if discount_percent > 60:
        print("Discount capped at 60%.")
        discount_percent = 60
        
    final_bill = price * (1 - (discount_percent / 100))
    
    return final_bill

print(apply_discount(1000, 10)) 
print(apply_discount(500))