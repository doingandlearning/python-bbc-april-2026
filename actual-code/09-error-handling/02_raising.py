user_input = input("Give me your age: ")

class AgeOutOfRangeError(Exception):
  pass

try:
  age = int(user_input)
  if age < 0 or age > 120:
    raise AgeOutOfRangeError("Age is too small or big")
  print(age)
except ValueError:
  print("Not a valid age, use only digits")
except AgeOutOfRangeError as e:
  print(e)