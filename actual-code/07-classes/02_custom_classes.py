user1 = {
  "name": "Michael",
  "location": "Salford",
  "team": "R&D AI Research"
}

user2 = {
  "name": "Gigi",
  "location": "London",
  "team": "Data Analytics"
}

def greet_user(user):
  print(f"Hello, {user.get("name")}, how are things in {user.get("location")}? Do you like working in the {user.get("team")} team?")



# created -> instantiated
class WebUser:
  def __init__(self, name, location, team):
    self.name = name
    if location in ["Glasgow", "London", "Salford", "Newcastle", "Cardiff"]:
      self.location = location
    else:
      self.location = None
      print("The location needs to be the BBC office you are attached to.")
    self.team = team
    self.responsibilities = []

  def greet(self):
    print(f"Hello, {self.name}, how are things in {self.location}? Do you like working in the {self.team} team?")
 
  def add_responsibility(self, responsibility):
    self.responsibilities.append(responsibility)

  def is_admin(self):
    """
    Is true when the user is a line manager
    """
    return "Line manager" in self.responsibilities

# WebUser -> __init__ (dunder init) -> Object
greet_user(user1)
greet_user(user2)
user3 = WebUser("Priya","London", "Testing")
user4 = WebUser(name="John", team="SWE", location="Glasgow")
print(user3.name)
print(user4.name)
user3.greet()
user4.greet()

user4.add_responsibility("write code")
user4.add_responsibility("test code")
user4.add_responsibility("go to standup")
user4.add_responsibility("Line manager")
print(user4.is_admin())


user3.is_admin()