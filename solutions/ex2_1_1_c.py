def molecular_weight(sequence):
    """Function that takes a single DNA sequence as an argument and estimates
    the molecular weight of this sequence.
    If the sequence passed in above contains N bases,
    use the mean weight of the other bases as the weight.
    """
    sequence = sequence.upper()
    base_weights = {'A': 331, 'C': 307, 'G': 347, 'T': 306}
    base_weights['N'] = sum(base_weights.values()) / len(base_weights)
    total_weight = 0
    for base in sequence:
        total_weight += base_weights[base]
    return total_weight

weight = molecular_weight("AAGGACTGTCNCGTNNCGTAGGATNATAGNN")
print("Moelacular weight:", weight, "g/mol")
