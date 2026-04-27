user_input = input("Enter your password: ")
password = "password123"
attempts_tried = 1

while user_input != password and attempts_tried < 3:
  print("Invalid password")
  user_input = input("Enter your password: ") 
  attempts_tried += 1

if attempts_tried < 3:
  print("here are you secret documents")
else:
  print("Exiting program. Failed authenication.")