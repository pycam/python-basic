lyrics = """
Imagine there's no Heaven
It's easy if you try
No Hell below us
Above us only sky

Imagine all the people
Living for today
Aaa haa

Imagine there's no countries
It isn't hard to do
Nothing to kill or die for
And no religion too

Imagine all the people
Living life in peace
Yoo hoo

You may say I'm a dreamer
But I'm not the only one
I hope someday you'll join us
And the world will be as one

Imagine no possessions
I wonder if you can
No need for greed or hunger
A brotherhood of man

Imagine all the people
Sharing all the world
Yoo hoo

You may say I'm a dreamer
But I'm not the only one
I hope someday you'll join us
And the world will live as one
"""

# Split into words
words = lyrics.split()
# Print the total number of words
print('There are', len(words), 'words in this song.')

# Print the number of unique words
unique_words = set(words)
print('There are', len(unique_words), 'unique ones.')

# Calculate the frequency of each word and store the result into a dictionary
results = {}
for w in unique_words:
    results[w.lower()] = lyrics.count(w)

# Print each unique word along with its frequency
for r in results:
    print(results[r], '\ttimes for word:', r)

# Find the most frequent word in the song
most_frequent = 0
for r in results:
    if results[r] > most_frequent:
        most_frequent = results[r]
        most_frequent_word = r

# Print the most frequent word with its frequency
print(most_frequent_word, 'is the most frequent word being used', most_frequent, 'times.')
