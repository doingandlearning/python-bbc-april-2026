class Shape:
  def __init__(self, type):
    self.type = type
  
  def __str__(self):
    return f"Shape of type {self.type}"

triangle = Shape("triangle")

def insecure_printer(message):
  print("I'm about to print")
  print(message)
  print("did i do okay? (insecurely)")

def main():
  print(f"Hello from the utils module! My name is {__name__}")

if __name__ == "__main__":
  main()