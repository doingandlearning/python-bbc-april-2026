import logging
import traceback
user_input = input("Give me a number: ")

logging.basicConfig(
    filename="app.log",
    level=logging.INFO, # INFO, WARN, ERROR, CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s"
)


try:
  user_number = int(user_input)
  print(100/user_number)
  # open("doesnotexist")
except ZeroDivisionError: 
  print("You can't divide by zero.")
except ValueError as e:
  print("Whoops! That wasn't a valid value.")
  print(e)
  logging.error(traceback.format_exc())
except Exception as e:
  print("Something unexpected happened. Please try again later.")
  print(traceback.format_exc())
else:
  print("Everything went fine!")
finally:
  print("This will always run")


print("This will run on error!")