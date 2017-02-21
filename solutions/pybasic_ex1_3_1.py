# Use the codon variables you defined previously
S = "TCT"
L = "CTT"
Y = "TAT"
C = "TGT"

# Create a list for the protein sequence CLYSY
codons = [C, L, Y, S, Y]

# Print the DNA sequence of the protein
print("DNA sequence:", codons)

# Print the DNA sequence of the last amino acid
print("Last codon:", codons[-1])

# Create two more variables containing the DNA sequence for a stop codon and a start codon
start = "ATG"
stop = "TGA"

# Replace the first element of the list with the start codon
codons[0] = start

# Append the stop codon to the end of the list
codons.append(stop)

# Print the resulting DNA sequence
print("DNA sequence after alteration:", codons)
