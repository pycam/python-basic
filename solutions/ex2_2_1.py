standardGeneticCode = {
          'UUU': 'Phe', 'UUC': 'Phe', 'UCU': 'Ser', 'UCC': 'Ser',
          'UAU': 'Tyr', 'UAC': 'Tyr', 'UGU': 'Cys', 'UGC': 'Cys',
          'UUA': 'Leu', 'UCA': 'Ser', 'UAA': None, 'UGA': None,
          'UUG': 'Leu', 'UCG': 'Ser', 'UAG': None, 'UGG': 'Trp',
          'CUU': 'Leu', 'CUC': 'Leu', 'CCU': 'Pro', 'CCC': 'Pro',
          'CAU': 'His', 'CAC': 'His', 'CGU': 'Arg', 'CGC': 'Arg',
          'CUA': 'Leu', 'CUG': 'Leu', 'CCA': 'Pro', 'CCG': 'Pro',
          'CAA': 'Gln', 'CAG': 'Gln', 'CGA': 'Arg', 'CGG': 'Arg',
          'AUU': 'Ile', 'AUC': 'Ile', 'ACU': 'Thr', 'ACC': 'Thr',
          'AAU': 'Asn', 'AAC': 'Asn', 'AGU': 'Ser', 'AGC': 'Ser',
          'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
          'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
          'GUU': 'Val', 'GUC': 'Val', 'GCU': 'Ala', 'GCC': 'Ala',
          'GAU': 'Asp', 'GAC': 'Asp', 'GGU': 'Gly', 'GGC': 'Gly',
          'GUA': 'Val', 'GUG': 'Val', 'GCA': 'Ala', 'GCG': 'Ala',
          'GAA': 'Glu', 'GAG': 'Glu', 'GGA': 'Gly', 'GGG': 'Gly'}

def protein_translation(sequence, geneticCode):
    """This function translates a nucleic acid sequence into a
    protein sequence, until the end or until it comes across
    a stop codon.
    """
    protein_sequence = []
    for i in range(0, len(sequence)-2, 3):
        codon = sequence[i:i + 3]
        codon.upper()

        # Convert DNA into RNA sequence
        if "T" in codon:
            # replace T by U
            codon = codon.replace('T', 'U')

        # Make sure the codon corresponds to a amino acid
        if codon in geneticCode:
            aminoAcid = geneticCode[codon]
        else:
            return codon + " codon not in dictionary of genetic code"

        # Break if stop codon is found
        if aminoAcid is None:
            break

        protein_sequence.append(aminoAcid)

    return protein_sequence


dna_sequence = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
print(dna_sequence)
protein_3letter_sequence = protein_translation(dna_sequence, standardGeneticCode)
print("".join(protein_3letter_sequence))
