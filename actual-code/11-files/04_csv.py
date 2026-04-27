import csv

with open("movies.csv") as file:
  # reader = csv.reader(file)
  reader = csv.DictReader(file)

  # next(reader)

  for row in reader:
    print(row)

with open("movies.csv", mode="a") as file:
  writer = csv.DictWriter(file, fieldnames=["Title", "Year", "Director", "Genre", "Revenue"])

  writer.writerow({
    "Title": "Project Hail Mary",
    "Director": "Phil Lord and Chris Miller",
    "Year": 2026,
    "Genre": "Sci-Fi",
    "Revenue": 0
  })
  