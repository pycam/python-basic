# Create a list where each element is an individual base of DNA.
# Make the array 15 bases long.
bases = ['A', 'T', 'T', 'C', 'G', 'G', 'T', 'C', 'A', 'T', 'G', 'C', 'T', 'A', 'A']

# Print the length of the list
print("DNA sequence length:", len(bases))

# Create a for loop to output every base of the sequence on a new line.
print("All bases:")
for base in bases:
    print(base)

# Create a while loop that starts at the third base in the sequence
# and outputs every third base until the 12th.
print("Every 3rd base:")
pos = 2
while pos <= 12:
    print(pos, bases[pos])
    pos += 3
