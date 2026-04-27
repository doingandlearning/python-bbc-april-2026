import requests


# request/response lifecycle

# Request -> url, method, headers, body, query params
# Methods/Verbs: GET, POST, DELETE, PUT, PATCH, OPTIONS, HEAD
# Headers: user-agent: chrome, location: northern ireland
# Query params:  ?q=bbc&name=kevin

# Response -> status code, headers, body
import csv
response = requests.get("https://swapi.dev/api/planets")
data = response.json()
planets = data.get("results")

with open("star_wars_planets.csv", mode="w") as file:
  writer = csv.DictWriter(file, fieldnames=["name", "rotation_period", "climate", "orbital_period"], extrasaction="ignore")
  writer.writeheader()

  for p in planets:
      writer.writerow({
        "name": p.get('name'),
        "rotation_period": p.get('rotation_period'),
        "climate": p.get("climate")
      })