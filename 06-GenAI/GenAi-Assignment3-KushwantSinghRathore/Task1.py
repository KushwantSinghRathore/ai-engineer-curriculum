# 1. Use a default value in the header (5 = 5%)
def apply_discount(price, discount_percent=5):
    
    if discount_percent > 60:
        print("Discount capped at 60%.")
        discount_percent = 60
        
    # 3. Calculate using the single-line formula we discussed!
    # Convert percentage to decimal by dividing by 100
    final_bill = price * (1 - (discount_percent / 100))
    
    return final_bill

# 4. Test it
print(apply_discount(1000, 10)) # Should return 900.0
print(apply_discount(500))      # Should return 475.0