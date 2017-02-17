# Read lyrics from file
with open('data/imagine.txt') as f:
    lyrics = f.read()
print(lyrics)

# Change all character to lower ones
lyrics = lyrics.lower()

# Split into words
words = lyrics.split()
print(words)

# Print the total number of words
print('There are', len(words), 'words in this song.')

# Print the number of distinct words
unique_words = set(words)
print('There are', len(unique_words), 'distinct words in this song.')

# Calculate the frequency of each word and store the result into a dictionary
results = {}
for w in unique_words:
    results[w.lower()] = words.count(w)

# Print each unique word along with its frequency
for r in results:
    print(results[r], '\t', r)

# Find the most frequent word in the song
most_frequent = 0
for r in results:
    if (results[r] > most_frequent) and (len(r) > 3):
        most_frequent = results[r]
        most_frequent_word = r

# Print the most frequent word with its frequency
print(most_frequent_word, 'is the most frequent word being used', most_frequent, 'times.')
