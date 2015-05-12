
def base_composition(seq):
    seq = seq.upper()
    num_As = seq.count('A')
    num_Cs = seq.count('C')
    num_Gs = seq.count('G')
    num_Ts = seq.count('T')

    return (num_As, num_Cs, num_Gs, num_Ts)

dna = "ACAGTGTCGTACAGATCAGTCAGATACA"

print base_composition(dna)

