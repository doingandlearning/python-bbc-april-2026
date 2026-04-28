def add(a,b,c=0,d=0):
  return a + b + c + d

add(1,2)
add(1,2,3)
add(1,2,3,4)

def add_tuple(numbers):
  total = 0
  for number in numbers:
    total = total + number
  return total

add_tuple((1,2,3,4))

def add_arbitrary(*numbers):  # ...
  print(numbers)
  total = 0
  for number in numbers:
    total = total + number
  return total

add_arbitrary(1,2,3)
add_arbitrary(1)
add_arbitrary()
add_arbitrary(1,2,3,4,5,6,7)  # *args

