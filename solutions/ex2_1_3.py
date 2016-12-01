def molecular_weight(sequence, molecule_type='DNA'):
    """Function that takes a single DNA or RNA sequence as an argument
    and estimates the molecular weight of this sequence.
    If the sequence passed in above contains N bases,
    use the mean weight of the other bases as the weight.
    Use an optional argument to specify the molecule type, but default to DNA.
    """
    sequence = sequence.upper()
    molecule_type = molecule_type.upper()

    dna_weights = {'A': 331, 'C': 307, 'G': 347, 'T': 306}
    rna_weights = {'A': 347, 'C': 323, 'G': 363, 'U': 324}

    if molecule_type == 'DNA':
        base_weights = dna_weights
    elif molecule_type == 'RNA':
        base_weights = rna_weights
    else:
        return "Unrecognised molecule_type " + molecule_type

    total_weight = 0
    for base in sequence:
        # check if base is a DNA base or not
        if base not in base_weights:
            return base + " is NOT a known DNA base"
        total_weight += base_weights[base]
    return total_weight


print("RNA weight:", molecular_weight("AACGUCGAAUCCUAGCGC", molecule_type="RNA"), "g/mol")
print("DNA weight:", molecular_weight("AACGTCGAATCCTAGCGC"), "g/mol")
print("Other sequence weight:", molecular_weight("AACGTCGAATXXXCCTAGCGC"), "g/mol")
