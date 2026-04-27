empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

#         -4       -3      -2       -1
#          0        1       2        3
names = ("Magda", "Tim", "Sanjiv", "Jay")

print(len(names))
print(names[3])
print(names[-1])
print(names[1:3])  # start:end (exclusive)
print(names[0:3:2])  # start : end : step
_, first, second, _ = names

for name in names:
  print(f"{name} works at the BBC.")

if "Kevin" in names:
  print("He is!")
else:
  print("He isn't!")

all_permissions = ("edit", "update", "archive", "create", "read")
my_permissions = ("read")

if "create" in my_permissions:
  print("Create new article")
else:
  print("You're not allowed to do that.")


print(names.count("Sean"))

print(names.index("Sanjiv"))

target = "Jay"

if target in names:
  print(f"{target} found at index {names.index(target)}")