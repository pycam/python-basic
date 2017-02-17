# Calculate GC content of a DNA sequence

# 15-base sequence you created for the previous exercise
bases = 'ATTCGGTCATGCTAA'

# Create a variable, gc, which we will use to count the number of Gs or Cs
gc = 0

# Output every base of the sequence alongside its index on a new line.
for i, base in enumerate(bases):
    print(i, base)

# Loop over the bases in your sequence.
# If the base is a G or a C, add one to your gc variable.
for base in bases:
    if (base == 'G') or (base == 'C'):
        gc += 1
print("Frequency of GC:", gc)

# Calculate the GC percentage and print it
gc_percent = (gc / len(bases)) * 100
print("%GC:", gc_percent)
