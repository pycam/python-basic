# Create a sequence where each element is an individual base of DNA.
# Make the array 15 bases long.
bases = 'ATTCGGTCATGCTAA'

# Create a while loop that starts at the third base in the sequence
# and outputs every third base until the 12th.
print("Every 3rd base:")
pos = 2
while pos <= 12:
    print(pos+1, bases[pos])
    pos += 3
