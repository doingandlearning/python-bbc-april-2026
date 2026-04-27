fruits = {"orange", "banana", "kiwi", "orange", "pear", "pear"}
print(fruits)
print(type(fruits))


print("orange" in fruits)

colours = {"green", "red", "blue", "orange"}

print(fruits.intersection(colours))

home_office = ["Salford", "Salford", "Cardiff", "London", "London", "Glasgow", "Belfast"]
print(list(set(home_office)))