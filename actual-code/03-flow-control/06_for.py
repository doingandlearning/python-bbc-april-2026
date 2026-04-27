target = int(input("What number do you want to search for? "))

for number_to_check in range(20):
  if number_to_check == target:
    print(f"Found it! It was {number_to_check}")
    break
  else:
    print(f"It wasn't {number_to_check}, still looking!")

for character in "This is a string":
  print(character)


for _ in range(3):
  print("hello!")