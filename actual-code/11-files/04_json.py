import csv
import json

with open("11-files/movies.csv") as file:
  reader = csv.DictReader(file)
  movies = []
  for row in reader:
    movies.append(row)
  
with open("11-files/movies.json", mode="w", newline="") as file:
  file.write(json.dumps(movies, indent=2))