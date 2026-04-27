empty_dictionary = {}
print(empty_dictionary)
print(type(empty_dictionary))

person = {
  "name": "Zoe",
  "role": "Senior Service Manager",
  "team": "Tech ops",
  "responsibilities": None,
  "birth_place": "Brighton"
}

print(person["name"])
person["responsibilities"] = ["service assurance", "governance"]

print(person)

for value in person:
  print(f"{value} is {person[value]}")

print("Zoe" in person)
print(person.values())
print(person.keys())
print(person.items())

for value in person.items():  # (key, value)
  print(f"{value[0]} is {value[1]}")

for key, value in person.items():  # unpacking
  print(f"{key} is {value}")

print(person.setdefault("birth_place", "Belfast"))
print(person)

data = {
  (57, 0): {},
  1: 2,
  "string": []
}