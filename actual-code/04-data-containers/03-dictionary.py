empty_dictionary = {}
empty_dictionary = dict()

print(empty_dictionary)
print(type(empty_dictionary))

user_dictionary = {
  "name": "Inken",
  "location": "Newcastle",
  "role": "Test engineer",
  "languages": ["Ruby", "TypeScript"] 
}



if "previous_role" in user_dictionary:
  print(user_dictionary["previous_role"])

print(user_dictionary.get("role", "Unknown")) # safe way to read from dictionary

for value in user_dictionary:
  print(f"{value} is {user_dictionary[value]}")

print(user_dictionary.keys())
print(user_dictionary.values())
print("Inken" in user_dictionary.values())
print(user_dictionary.items())

for key, value in user_dictionary.items():
  print(f"{key} is {value}")

print(user_dictionary.setdefault("role", "Juggler"))
print(user_dictionary)