import traceback
# user input, file, network, database
user_input = input("Give me a number: ")

try:
  user_number = int(user_input)
  print(100 / user_number)
except ValueError as e: 
  print("Whoops! That wasn't a number, you need to use digits.")
  print("=" * 10)
  print(f"ValueError: {e}") # writing to log
except ZeroDivisionError:
  print("Uh oh! You can't divide by zero.")
  print("=" * 20)
  print(traceback.format_exc())
except Exception:
  print("Whoops! Something unexpected happened")
  print("=" * 20)
  print(traceback.format_exc())
else:
  print("When nothing went wrong!")
finally:
  print("Will always run and will run last.")

print("This will be printed!")