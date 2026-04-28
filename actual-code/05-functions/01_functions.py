def print_message_with_borders(message, border_symbol="=", border_length=10):
  """
  A function that prints a message with borders.
  How? Why? When not? What to remember.
  """
  print(border_symbol * border_length)
  print(message)
  print(border_symbol * border_length)

# print_message_with_borders("Hello from Salford", border_length=18)  # invoking/calling the function
# print_message_with_borders("Hello from Glasgow", "-", 18)  # invoking/calling the function
# print_message_with_borders("Hello from Newcastle", "+", 20)  # invoking/calling the function
# print_message_with_borders(border_symbol="🥊", message="Hello from London",  border_length=9)  # invoking/calling the function


def get_message_with_borders(message, border_symbol="=", border_length=10):
  """
  A function that prints a message with borders.
  How? Why? When not? What to remember.
  """
  output = f"""{border_symbol * border_length}
{message}
{border_symbol * border_length}"""

  return output

print(get_message_with_borders("Hello from Salford", border_length=18))  # invoking/calling the function)
get_message_with_borders("Hello from Glasgow", "-", 18)  # invoking/calling the function
get_message_with_borders("Hello from Newcastle", "+", 20)  # invoking/calling the function
get_message_with_borders(border_symbol="🥊", message="Hello from London",  border_length=9)  # invoking/calling the function