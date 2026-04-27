headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom",
    "UK inflation rate falls to lowest level in three years",
    "New David Hockney exhibition opens in London",
    "Science discovers new way to tackle plastic waste",
    "Government announces new funding for NHS",
    "Stock market hits record high on tech boom",
    "Debate rages over future of Artificial Intelligence",
    "Classic Doctor Who episodes to be released in colour"
]

# mean -> total number of words / total of headlines
total_number_of_headlines = len(headlines)

total_number_of_words = 0
for h in headlines:
  total_number_of_words += len(h.split())

total_words = sum(len(h.split()) for h in headlines)

print(total_number_of_words / total_number_of_headlines)


user_input = " " + input("What keyword do you want to search for? ").lower() + " "

matching_headlines = []

for h in headlines:
  if f" {h.lower()} ".find(user_input) > -1:
    matching_headlines.append(h)

matching_headlines = []
for h in headlines:
  if user_input in h.lower():
    matching_headlines.append(h)

matches = [h for h in headlines if user_input in h.lower()]  # list comprehension!


print(f"Your keyword ({user_input}) was found in {len(matching_headlines)} headlines.")
print(matching_headlines)
