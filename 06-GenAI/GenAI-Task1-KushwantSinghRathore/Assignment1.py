#Task 1

products = ["Mango","Apple","Banana","Pomogranate","Strawberry","Papaya"]
sample_product = ("Mango",100,"Fruit")
print(products[1])
print(products[-1])
products.append("Lichi")
products.append("Kiwi")
print(products)

#Task 2

categories = ["Tropical", "Standard", "Tropical", "Berry", "Berry", "Tropical", "Tropical", "Tropical"]
categories_set = set(categories)
categories_set.add("Citrus")
categories_set.add("Berry")
print(categories_set)
print("Citrus" in categories_set)
print(len(categories_set))

#Task 3

price_dict = {"Mango":20,
              "Apple":15,
              "Banana":100,
              "Pomogranate":50,
              "Strawberry":25,
              "Papaya":45}
price_dict["Lichi"] = 5
price_dict["Kiwi"] = 35
price_dict["Mango"] = 30
print(price_dict)

if "Shoe" in price_dict:
    price_dict.pop("Shoe")
else:
    print("Product not found")

avg_price = sum(price_dict.values())/ len(price_dict)
print(avg_price)


# Task 4


catalog = []
for prod, cat in zip(products,categories):
    price = price_dict[prod]
    catalog.append((prod,price,cat))
    
print(catalog)

category_to_products = {}

for prod, price, cat in catalog:
    
    if cat not in category_to_products:
        
        category_to_products[cat] = [prod]
        
    else:
        
        category_to_products[cat].append(prod)

print(category_to_products)

max_category = ""
max_count = 0

for cat, prod_list in category_to_products.items():
    if len(prod_list) > max_count:
        max_count = len(prod_list)
        max_category = cat
print(category_to_products[max_category])