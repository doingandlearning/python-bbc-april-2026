user_input = input("Give me a number: ")

while not user_input.isdigit():
  print("You need give me just numbers.")
  user_input = input("Give me a number: ")

user_number = int(user_input)
print(f"One more than that is {user_number + 1}")
