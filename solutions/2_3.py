bases = ['A', 'T', 'T', 'C', 'G', 'G', 'T', 'C', 'Y', 'T', 'G', 'C', 'T', 'A', 'A']

gc = 0.0

for base in bases:

    if base not in "ACGT":
        raise Exception('Invalid DNA nucleotide: "%s"' % base)

    if base == 'G':
        gc += 1
    elif base == 'C':
        gc += 1
    

gc_percent = 100 * (gc / len(bases))

print "%GC:", gc_percent
