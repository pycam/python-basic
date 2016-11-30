def base_composition(sequence):
    """Write a function that counts the number of each base found
    in a DNA sequence.
    """
    sequence = sequence.upper()
    num_As = sequence.count('A')
    num_Cs = sequence.count('C')
    num_Gs = sequence.count('G')
    num_Ts = sequence.count('T')
    # Return the result as a tuple of 4 numbers representing the counts of each base A, C, G and T.
    return (num_As, num_Cs, num_Gs, num_Ts)

dna = "ACAGTGTCGTACAGATCAGTCAGATACA"
print('base composition', base_composition(dna))
