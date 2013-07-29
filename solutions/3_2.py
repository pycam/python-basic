import sys

def molecular_weight(sequence, molecule_type = 'DNA'):
    sequence = sequence.upper()
    molecule_type = molecule_type.upper()

    dna_weights = {'A': 331, 'C': 307, 'G': 347, 'T': 306}
    rna_weights = {'A': 347, 'C': 323, 'G': 363, 'U': 324}

    if molecule_type == 'DNA':
        base_weights = dna_weights
    elif molecule_type == 'RNA':
        base_weights = rna_weights
    else:
        raise Exception("Unrecognised molecule_type: %s" % molecule_type)

    total_weight = 0
    for base in sequence:
        total_weight += base_weights[base]
    return total_weight

if len(sys.argv) != 3:
    print "Usage: %s <molecule_type> <sequence>" % sys.argv[0]
    sys.exit(0)

weight = molecular_weight(molecule_type = sys.argv[1], sequence = sys.argv[2])

print "Weight:", weight, "g/mol"

