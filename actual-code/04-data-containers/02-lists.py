empty_list = []
empty_list = list()
print(empty_list)
print(type(empty_list))

beatles = ["John", "Paul", "George", "Ringo"]

# Create/Add things to our list
beatles.append("Edith")  # Adds one element
print(beatles)

beatles.extend(("Michael", "Priya", "Gigi")) # Adding multiple items
print(beatles)

beatles.insert(2, "Tom")
print(beatles)

# Read
print(beatles[0])
print(beatles[0:4])

member = beatles.pop(0)  # First In, First Out (FILO) / Last In Last Out (LILO)
print(member)
print(beatles)

# Update
beatles[4] = "John"
beatles[5] = "John"
print(beatles)

# Delete
del beatles[0:2]
print(beatles)

while "John" in beatles:
  beatles.remove("John")

print("John" in beatles)
if "John" in beatles:
  print(beatles.index("John"))
print(beatles.count("John"))

for member in beatles:
  print(f"{member} is a surviving member of our beatles tribute band.")

beatles.reverse()
print(beatles)

new_beatles = beatles.copy()
new_beatles.append("John")
print(new_beatles)
print(beatles)