# Check if a DNA sequence contains a stop codon

# DNA sequence given
dna = "GTT GCA CCA CAA CCG TAG TAA TGA"

# Check if the sequence contains one possible stop codon
if "TAG" in dna:
    print("TAG found")

# Check if the sequence contains any of the 3 stop codons
if ("TAG" in dna) or ("TAA" in dna) or ("TGA" in dna):
    print("Stop codon found")
