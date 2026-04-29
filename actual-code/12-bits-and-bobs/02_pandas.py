import pandas as pd

# DataFrame -> in memory spreadsheet
# Series -> Column in your spreadsheet
df = pd.read_csv("movies.csv")

# Get to the know the data
print(df.head())
print(df.tail())
print(df.sample(5))
print(df.info())
print(df.describe())

df["years_since_release"] = 2026 - df["Year"]  # Projecting/Vectorising
print(df)

print(df[["Title", "years_since_release"]])
print(df[df["years_since_release"] < 10])  # Masking

df[df["years_since_release"] < 10].to_csv("recent_movies.csv")