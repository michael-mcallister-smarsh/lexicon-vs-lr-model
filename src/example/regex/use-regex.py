import re

with open("sport_dataset.txt", 'r') as file:
    # Read all lines and strip whitespace
    sport_words = [line.strip() for line in file if line.strip()]

print(f"Loaded {len(sport_words)} words from lexicon.")
# Escape any special regex characters in the words
escaped_words = [re.escape(word) for word in sport_words]
# Join words with | (OR operator in regex)
pattern = r'\b(?:' + '|'.join(escaped_words) + r')\b'
regex = re.compile(pattern, re.IGNORECASE)

while True:
    sentence = input("Enter a sentence: ")
    # Preprocess the input sentence
    matches = regex.findall(sentence)
    if matches:
        print(f"Found {len(matches)} sports-related terms: {', '.join(matches)}")
    else:
        print("No sports-related terms found.")
