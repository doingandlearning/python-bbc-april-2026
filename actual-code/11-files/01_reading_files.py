import pathlib
file_path = pathlib.Path(__file__).parent / "test.txt"

file = open(file_path)

contents = file.read()
print(contents)
print(type(contents))

file.seek(0)
contents = file.readlines()
print(contents)
print(type(contents))

file.seek(0)
line = file.readline()
while line:
  print(line)
  line = file.readline()


file.close()