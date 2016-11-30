def gc_content(sequence):
    """Calculate the GC content of a DNA sequence
    """
    gc = 0
    for base in sequence:
        if (base == 'G') or (base == 'C'):
            gc += 1
    return 100 * (gc / len(sequence))


#print('GC%', gc_content('ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'))
