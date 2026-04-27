is_sunny = True
temp_in_celcius = 24
has_airconditioning = False

if is_sunny and temp_in_celcius > 20:
  if has_airconditioning:
    print("Turn on the airconditioning (sorry planet!)")
  else:
    print("Try not to melt!")
  print("It's nice outside!")

# cyclomatic complexity