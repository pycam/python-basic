genetic_code = {
    "GTT": "Val",
    "GCA": "Ala",
    "CCA": "Pro",
    "CAA": "Glu",
    "CCG": "Pro"
}

codon_string = "GTT GCA CCA CAA CCG"

codon_list = codon_string.split()

print codon_list[0], "codes for", genetic_code[codon_list[0]]
print codon_list[1], "codes for", genetic_code[codon_list[1]]
print codon_list[2], "codes for", genetic_code[codon_list[2]]
print codon_list[3], "codes for", genetic_code[codon_list[3]]
print codon_list[4], "codes for", genetic_code[codon_list[4]]

