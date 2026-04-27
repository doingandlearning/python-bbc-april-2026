def add(a, b):
  return a + b

class Shape:
  def __init__(self, type):
    self.type = type

triangle = Shape("triangle")

if __name__ == "__main__":
  print(f"Hello from the {__name__} module!")