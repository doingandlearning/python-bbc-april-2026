user_input = input("Enter your password: ")
password = "password123"
attempted_tries = 1

# uncounted loop - we don't know how many times it's going to run before it starts
while user_input != password and attempted_tries < 3:
  print("Unauthorized. Please try again.")
  user_input = input("Enter your password: ")
  attempted_tries = attempted_tries + 1
  # attempted_tries += 1

if attempted_tries < 3:
  print("Here are your secret documents.")