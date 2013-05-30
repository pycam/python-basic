
S = "TCT"
L = "CTT"
Y = "TAT"
C = "TGT"

codons = [C, L, Y, S, Y]

print "Codon sequence:", " ".join(codons)

print "Last codon:", codons[-1]

start = "ATG"
stop = "TGA"

codons[0] = start
codons.append(stop)

print "DNA sequence after alteration:", "".join(codons)
