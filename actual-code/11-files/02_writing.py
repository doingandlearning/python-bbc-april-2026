from datetime import datetime

with open("test.log", mode="a") as f:
  f.write(f"{datetime.now()} - Program started\n")

file = open("log.txt", mode="a")

file.write("Hello!\n")
file.write("How are you?\n")
file.write("I'm doing well :)\n")


file.close()

# Pythonic -> Idiomatic Python
with open("test.log", mode="a") as f:
  f.write(f"{datetime.now()} - Program ended\n")
