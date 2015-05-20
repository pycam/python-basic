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


def protein_translation(seq, geneticCode):
    """ This function translates a nucleic acid sequence into a
    protein sequence, until the end or until it comes across
    a stop codon
    """
    proteinSeq = []
    i = 0
    while i + 2 < len(seq):
        codon = seq[i:i + 3]
        codon.upper()
        
        # Check you have RNA sequence
        if "T" in codon:
            # raise Exception("Expected RNA sequence, but found T in a codon")
            codon = codon.replace('T', 'U')  # or just replace instead of raising the exception
        
        # Make sure the codon corresponds to a amino acid
        try:
            aminoAcid = geneticCode[codon]
        except KeyError, e:
            print e
            raise KeyError("codon %s not in dictionary of genetic code" % codon)

        # Break if stop codon is found
        if aminoAcid is None:  # Found stop codon
            break
    
        proteinSeq.append(aminoAcid)
        i += 3
    
    return proteinSeq

dnaSeq = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
print dnaSeq
protein3LetterSeq = protein_translation(dnaSeq, standardGeneticCode)
print protein3LetterSeq