first_name = "Kevin"
last_name = "Cunningham"

# concatenate strings -> join together
full_name = first_name + " " + last_name
print(full_name)

print("1 + 1 = " + str(2))

full_name = f"{ first_name } { last_name }"

# f-string -> formatted string
print(f"{first_name} {last_name}")
print(f"1 + 1 = {1 + 1}")
print(f'4 x 5 = {4 * 5}')
print("""First line
Second line
Third line""")

print(full_name.upper())
# full_name = full_name.upper()
print(full_name.lower())
print(full_name.count("n"))
print(full_name.center(100))
print(full_name.ljust(100))
print(full_name.rjust(100))

print(full_name.lower().find("kevin"))


# 0123456789
# Kevin Cunningham
print(full_name.find("not there"))

print(full_name.find("not there") == -1)

print(full_name.replace("in", "on"))