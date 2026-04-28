locations = ["London", "Glasgow", "Salford", "Newcastle", "Belfast"]

upper_cased_locations = []

for location in locations:
  if "a" in location:
    transformed_location = location.upper()  # some kind of transformation
    upper_cased_locations.append(transformed_location)

print(upper_cased_locations)

def get_upper_case_version(original):
  return original.upper()

# map() 
list_comp_upper_case = [l.upper() for l in locations if "a" in l]
print(list_comp_upper_case)