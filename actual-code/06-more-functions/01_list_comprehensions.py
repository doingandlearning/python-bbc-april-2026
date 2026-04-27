# Product data: (name, price, category, stock, sales)
products = [
    ("Wireless Mouse", 29.99, "Electronics", 50, 120),
    ("USB-C Cable", 12.99, "Electronics", 100, 85),
    ("Desk Lamp", 45.00, "Furniture", 25, 30),
    ("Notebook Set", 18.50, "Stationery", 75, 45),
    ("Keyboard", 79.99, "Electronics", 30, 60),
    ("Monitor Stand", 35.00, "Furniture", 40, 25),
]  

product_names = []

for p in products:
  product_names.append(p[0])

print(product_names)

# List Comprehension
product_names = [p[0] for p in products]
print(product_names)

def calculate_price_with_tax(price, tax_as_decimal=0.2):
  percentage_multiplier = 1 + tax_as_decimal  
  new_price = price * percentage_multiplier
  rounded_price = round(new_price, 2)
  return rounded_price 

product_prices_with_tax = []

for p in products:
  product_prices_with_tax.append(calculate_price_with_tax(p[1]))

print(product_prices_with_tax)

print([calculate_price_with_tax(p[1]) for p in products])