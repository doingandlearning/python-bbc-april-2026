def add(a,b):
  return a + b

add = lambda a,b: a + b

products = [
    ("Wireless Mouse", 29.99, "Electronics", 50, 120),
    ("USB-C Cable", 12.99, "Electronics", 100, 85),
    ("Desk Lamp", 45.00, "Furniture", 25, 30),
    ("Notebook Set", 18.50, "Stationery", 75, 45),
    ("Keyboard", 79.99, "Electronics", 30, 60),
    ("Monitor Stand", 35.00, "Furniture", 40, 25),
] 

def find_price_from_product(p):
  return p[1]


most_expensive = max(products, key=find_price_from_product)
most_expensive = max(products, key=lambda p: p[1])
print(most_expensive)