import sys

def gc_content(seq):
    seq = seq.upper()
    return ( ( seq.count('G') + seq.count('C') ) / float(len(seq)) ) * 100

if len(sys.argv) < 2:
    print "Please supply some DNA sequence"
    sys.exit(0)

print "GC%:", gc_content(sys.argv[1])

