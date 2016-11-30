import sys


def gc_content(seq):
    for base in seq:
        if base not in "ACGT":
            raise Exception('Invalid DNA nucleotide: "%s"' % base)
    seq = seq.upper()
    return ((seq.count('G') + seq.count('C')) / float(len(seq))) * 100

if len(sys.argv) < 2:
    print("Please supply some DNA sequence")
    sys.exit(0)

try:
    print("GC%:", gc_content(sys.argv[1]))
except Exception as e:
    print(e)


