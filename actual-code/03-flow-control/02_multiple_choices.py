user_input = input("What channel would you like to watch? ").lower().strip()

if user_input == "bbc1":
  print("BBC One: Where the nation gathers to watch people bake, dance or betray each other.")
elif user_input == "bbc2":  # else if -> elif
  print("BBC Two: for when you want to feel slightly more intellectual about your evening.")
elif user_input == "cbeebies" or user_input == "cbbc":
  print("Time for the kids to watch some TV.")
elif user_input.startswith("bbc") and user_input.find("news") > -1:
  print("Are you sure you want the news? Maybe some YT Shorts instead?")
elif user_input.startswith("bbc"):
  print("Still in the family. The BBC has more channels than you'd think.")
elif not user_input.startswith("bbc"):
  print("Not around here.")
else:
  print("Never heard of it. Are you sure you haven't made that up?")


match user_input:
  case "bbc1":
    print("BBC One: where the nation gathers to watch people bake, dance, or betray each other.")
  case "bbc2":
    print("BBC Two: for when you want to feel slightly more intellectual about your evening.")
  case "bbc3":
    print("BBC Three: back on telly and pretending it never left.")
  case _:
    print("Never heard of it. Are you sure you haven't made that up?") 


