def get_word_count(headline):
  return len(headline.split())


headlines =[]
short_headlines = [h for h in headlines if 3 < get_word_count(h) <= 7 ]

specific_headline_lengths = [
  len(h.split())
  for h in headlines
  if "new" in h.lower() or "tax" in h.lower()
]