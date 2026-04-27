def add(a, b):
  #  ([], []),
  # if a is not a int or float raise a typeerror
  if not isinstance(a, (int, float)):
    raise TypeError("a must be a int or float")
  if not isinstance(b, (int, float)):
    raise TypeError("b must be a int or float")

  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError("Arguments must be a ints or floats")
  return a + b

# something_test.py

# test_something.py