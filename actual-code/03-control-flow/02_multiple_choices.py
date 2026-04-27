channel = input("What channel do you want to watch? ").lower().strip()

if channel == "bbc1":
  print("Are you looking forward to the next season of traitors?")
  print("or something else")
elif channel == "bbc2":  # else if -> elif
  print("Do you watch University Challenge?")
elif channel == "cbeebies" or channel == "cbeebies -1":
  print("Time for Bluey?")
elif channel.endswith("news") and channel.startswith("bbc"):
  print("Are you sure? Python is nicer than the news.")
elif channel.startswith("sky"):
  print("We don't like your kind around here.")
else:
  print("I don't know that channel.")