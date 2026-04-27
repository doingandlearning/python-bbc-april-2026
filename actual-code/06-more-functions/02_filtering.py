# Product data: (name, price, category, stock, sales)
products = [
    ("Wireless Mouse", 29.99, "Electronics", 50, 120),
    ("USB-C Cable", 12.99, "Electronics", 100, 85),
    ("Desk Lamp", 45.00, "Furniture", 25, 30),
    ("Notebook Set", 18.50, "Stationery", 75, 45),
    ("Keyboard", 79.99, "Electronics", 30, 60),
    ("Monitor Stand", 35.00, "Furniture", 40, 25),
]  

electronic_products = []

for p in products:
  if p[2] == "Electronics":
    electronic_products.append(p)

print(electronic_products)

electronic_products = [p for p in products if p[2] == "Electronics"]

cheap_products = []

for p in products:
  if p[1] < 30:
    cheap_products.append(p)

cheap_products = [p for p in products if p[1] < 30]