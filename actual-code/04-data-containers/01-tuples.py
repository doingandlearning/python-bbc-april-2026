empty_tuple = ()
empty_tuple = tuple()

print(empty_tuple)
print(type(empty_tuple))

#          0        1      2        3       4
#          -5       -4     -3       -2       -1
names = ("John", "Tom", "Edith", "Gigi", "Inken")

print(names[3])  # accessing by index
print(names[2:4])  # starting at 2, upto but not including 4
print(names[:2])
print(names[2:])
print(names[1:4:2])
print(names[::-1])
print(names[-1])

print("John" in names)
print("Michael" in names)

for person in names:
  print(f"{person} works at the BBC")

print(len(names))

print(names.count("John"))
print(names.count("Michael"))

print(names.index("John"))

if "Kevin" in names:
  print(names.index("Kevin"))
else:
  print("Kevin not in names")

more_names = ("Michael", "Edith", "Priya")

all_the_names = (names, more_names, "Kevin")
print(all_the_names[1][2])

channels = ("bbc1", "bbc2")

first_channel = channels[0]
second_channel = channels[1]

# unpacking -> destructuring
first_channel, = channels
print(f"First channel: {first_channel}, Second channel: {second_channel}")