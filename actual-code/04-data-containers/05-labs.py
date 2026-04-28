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

total_words = sum(len(h.split()) for h in headlines)
print(total_words)

total_words = 0

for headline in headlines:
  word_list = headline.split()
  words_in_headline = len(word_list)
  total_words = total_words + words_in_headline

print(total_words/len(headlines))

user_keyword = input("What do you want to search for? ").lower()
matches = []
for headline in headlines:
  if user_keyword in headline.lower():
    matches.append(headline)

print(f"Found {len(matches)} matches.")
print(matches)



things_on_desk = ["Keyboard", "Cup", "Monitor", "Laptop"]
things_on_desk.append("Kindle")
things_on_desk.remove("Cup")

things_on_desk = ("Keyboard", "Cup", "Monitor", "Laptop")