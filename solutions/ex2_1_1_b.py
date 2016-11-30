def molecular_weight(sequence):
    """Function that takes a single DNA sequence as an argument and estimates
    the molecular weight of this sequence.
    """
    sequence = sequence.upper()
    base_weights = {'A': 331, 'C': 307, 'G': 347, 'T': 306}
    total_weight = 0
    for base in sequence:
        total_weight += base_weights[base]
    return total_weight

# Test your function using some example sequences.
weight = molecular_weight("ACTTGGGCAGATAGTCGCG")
print("Molecular weight:", weight, "g/mol")
