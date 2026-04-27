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

new_headlines = [h for h in headlines if "new" in h.lower()]

print(new_headlines)

# tax, stock

keywords = ["tax", "stock"]

tax_stock_headlines = [
  h for h in headlines
  if any(k in h.lower() for k in keywords)  # vs all
]

# [False, False]
# [True, False]

print(tax_stock_headlines)

new_list = []

for h in headlines:
  for k in keywords:
    if k in h.lower():
      new_list.append(h)
    
structured = [
    {
        "headline": h,
        "word_count": len(h.split()),
        "has_new": "new" in h.lower()
    }
    for h in headlines
]
import pprint
pprint.pprint(structured)