from custom_errors import InvalidChannelError

user_input = input("What channel? ").lower().strip()

try:
  if user_input not in ["bbc1", "bbc2", "cbeebies", "cbcc"]:
    raise InvalidChannelError(f"This is not a valid channel: {user_input}")
  int("a")
except ValueError as e:
  print("Not a valid channel. Stay in the BBC")
except InvalidChannelError as e:
  print(e)