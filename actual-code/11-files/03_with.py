file = open("test.log", mode="a")

file.write("Python is cool\n")
file.write("So is text\n")

file.close()

with open("test.log", mode="a") as f:
  f.write("Do you like this any better?\n")
