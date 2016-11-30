# DNA sequence given
codon_string = "GTT GCA CCA CAA CCG"

# Split this string into the individual codons
codon_list = codon_string.split()

# Dictionnary to map between codon sequences and amino acids they encode
genetic_code = {
    "GTT": "Val",
    "GCA": "Ala",
    "CCA": "Pro",
    "CAA": "Glu",
    "CCG": "Pro"
}

# Print each codon and its corresponding amino acid
print(codon_list[0], "codes for", genetic_code[codon_list[0]])
print(codon_list[1], "codes for", genetic_code[codon_list[1]])
print(codon_list[2], "codes for", genetic_code[codon_list[2]])
print(codon_list[3], "codes for", genetic_code[codon_list[3]])
print(codon_list[4], "codes for", genetic_code[codon_list[4]])
