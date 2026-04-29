file = open("11-files/test.txt")

# <_io.TextIOWrapper name='11-files/test.txt' mode='r' encoding='UTF-8'>
# file handle ... __str__

contents = file.read()  # Returns the whole of the file as a str!
print(contents)
print(type(contents))

file.seek(0)
contents = file.readlines()  # Returns the whole file as a list of lines.
contents = [line.strip() for line in contents]
print(contents)
print(type(contents))

# Mobile\nKindle\nWatch\nWire snippers\nPen
for line in contents:
  print(line.strip())

file.seek(0)
# Lazy/Generator approach
line = file.readline().strip()  # line by line -> cheaper in memory

while line:
  print(line)
  line = file.readline().strip()

file.seek(0)
print("=" * 100)
things_the_letter_a = []

for line in file:
  if "a" in line:
    things_the_letter_a.append(line.strip())

print(things_the_letter_a)
