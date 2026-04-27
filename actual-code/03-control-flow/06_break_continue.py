user_input = int(input("What number do you want to look for? "))

for number in range(100):
  if user_input == number:
    print("Found it!")
    break
  else:
    print(f"It wasn't {number}, still looking for {user_input}")

for number in range(10):
  if number % 2 == 0:
    continue
  print(f"We like odd numbers like {number}")