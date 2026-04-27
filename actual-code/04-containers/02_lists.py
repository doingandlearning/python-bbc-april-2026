empty_list = []
print(empty_list)
print(type(empty_list))

beatles = ["John", "Paul", "George", "Ringo"]

# Read 
print(beatles[0])

for band_member in beatles:
  print(band_member)

print("Kevin" in beatles)
print("Ringo" in beatles)
print(len(beatles))

# Create 
beatles.append("Holly")  # one item
print(beatles)

beatles.extend(("Sean", "Catherine", "Matina"))  # multiple items
print(beatles)

beatles.insert(1, "Emily") # item at specific position
print(beatles)

# Read

# Last in, first out

band_member_to_email = beatles.pop()  # last member
band_member_to_email = beatles.pop(0)  # first member
print(beatles)

# 
# Update 
beatles[1] = "Tim"
print(beatles)

# Delete 
del beatles[2:4]
print(beatles)


new_beatles = beatles.copy()
new_beatles.append("Jay")

beatles.append("Catherine")
print(new_beatles)
print(beatles)

while "Catherine" in beatles:
  print(f"Catherine found at {beatles.index("Catherine")}")
  beatles.remove("Catherine")

print(beatles)

beatles.sort()
print(beatles)

beatles.reverse()
print(beatles)