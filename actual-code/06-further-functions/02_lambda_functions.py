# lambda -> arrow function/callable/anonymous function

def add(a,b):
  print("I am adding things up!")
  return a + b

add_lambda = lambda a,b: a + b

print(add(1,2))
print(add_lambda(1,2))

people = [
    {"name": "Alice",   "age": 34, "score": 82},
    {"name": "Bob",     "age": 28, "score": 91},
    {"name": "Charlie", "age": 41, "score": 67},
    {"name": "Diana",   "age": 30, "score": 88},
    {"name": "Eve",     "age": 22, "score": 95},
]
locations = ["London", "Glasgow", "Salford", "Newcastle", "Belfast"]

def get_age(person):
  return person.get("age", 0)

def get_score(person):
  return person.get("score", 0)

def get_city(person):
  return person.get("user", {}).get("address", {}).get("city", "Unknown")

print(sorted(people, key=get_score))
print(sorted(people, key=lambda person: person.get("score", 0)))

def get_heading(document):
  return document.getElementById("...")

# selector=get_heading


# selector=lambda document: document.getElementById("...")

# Short, simple tasks
# Throwaway
# Passed in as arguments

# pandas