import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
response.raise_for_status()
data = response.json()

with open("pikachu.json", mode="w", newline="") as file:
  file.write(json.dumps(data, indent=2))