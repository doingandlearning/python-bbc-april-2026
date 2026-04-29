import csv

# reader, DictReader
# writer, DictWriter

with open("11-files/movies.csv") as file:
  reader = csv.reader(file)
  next(reader)
  for title, year, _, _ in reader:
    if int(year) > 2020:
      print(f"{title} was released in {year}")

with open("11-files/movies.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    if int(row.get("Year", 0)) > 2020:
      print(f"{row.get("Title")} was released in {row.get("Year")}")

# with open("11-files/movies.csv", mode="a") as file:
#   writer = csv.writer(file)
#   writer.writerow(["Project Hail Mary", "2026", "Phil Lord, Chris Miller", "Sci-fi"])

with open("11-files/movies.csv", mode="a") as file:
  writer = csv.DictWriter(file, fieldnames=["Title", "Year", "Director", "Genre"])
  writer.writerow({
    "Director": "Robert Luketic",
    "Title": "Legally Blonde",
    "Year": "2001",
    "Genre": "Comedy"
  })