first_name = "Kevin"
last_name = "Cunningham"

# concatenate -> join together
full_name = first_name + " " + last_name
print(full_name)
print("Hello " + first_name + ", how are you today?")
print("Hello " + first_name + ", I've heard your favourite number is " + str(42))

my_favourite_number = 42
print(f"Hello {first_name}, I've heard your favourite number is {my_favourite_number}.")

print("This is also a string. Isn't it nice")
print('He said, "I like Python".')

# triple quotes
print(f'''{first_name} said, "Isn't Python great!"
She said, "I think it's great too"
1 + 1 = {1 + 1}''')

print(len(first_name))
print(first_name.upper())
print(first_name.center(30))
print(first_name.ljust(30))
print(first_name.rjust(30))

# 01234
# Kevin
print(first_name.find("qweqweqw"))

print(first_name.isalpha())
print(first_name.isdigit())

print(first_name.count("i"))