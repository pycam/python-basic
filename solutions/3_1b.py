import sys

def molecular_weight(sequence):
    sequence = sequence.upper()
    base_weights = {'A': 331, 'C': 307, 'G': 347, 'T': 306}
    total_weight = 0
    for base in sequence:
        total_weight += base_weights[base]
    return total_weight

weight = molecular_weight("ACTTGGGCAGATAGTCGCG")

print "Weight:", weight, "g/mol"

