# Calculate GC content of a DNA sequence

# 15-base array you created for the previous exercise
bases = ['A', 'T', 'T', 'C', 'G', 'G', 'T', 'C', 'A', 'T', 'G', 'C', 'T', 'A', 'A']

# Create a variable, gc, which we will use to count the number of Gs or Cs in our sequence
gc = 0

# Loop over the bases in your sequence.
# If the base is a G or a C, add one to your gc variable.
for base in bases:
    if (base == 'G') or (base == 'C'):
        gc += 1
print("Frequency of GC in the sequence:", gc)

# Calculate the GC percentage and print it
gc_percent = 100 * (gc / len(bases))
print("%GC:", gc_percent)
