def reverse_complement(sequence):
    """Write a function to return the reverse-complement of a nucleotide
    sequence.
    """
    reverse_base = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    sequence = sequence.upper()
    sequence = reversed(sequence)
    result = []
    for base in sequence:
        # check if sequence is a DNA sequence or not
        if base not in 'ATCG':
            return base + " is NOT a known DNA base"
        result.append(reverse_base[base])
    return "".join(result)

print(reverse_complement('ATCGTAGCatgcAATTGGC'))
print(reverse_complement('ATCGTAGCatgcxAATTGGC'))
