def print_message_with_top_and_bottom_dividers(message, divider="=", divider_length=None):
  """
  A function to print a message with dividers at the top and bottom
  """
  if divider_length is None:
    divider_length = len(message)

  print(divider * divider_length)
  print(message)
  print(divider * divider_length)



print_message_with_top_and_bottom_dividers(divider="*", message="Hello from line 6", divider_length=30)  
print_message_with_top_and_bottom_dividers("Python is cool!", "-")  
print_message_with_top_and_bottom_dividers("🐍🐍🐍🐍🐍", divider_length=10)

# Domain Driven Design
