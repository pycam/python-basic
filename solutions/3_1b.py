import sys

def gc_content(seq):
    gc = 0.0
    for base in seq:
        if base in "GC":
            gc += 1
    gc_content = 100 * (gc / len(seq))
    return gc_content

if len(sys.argv) != 2:
    print "Please supply a DNA sequence"
    sys.exit(0)

seq = sys.argv[1]

gc_percent = gc_content(seq)

print "%GC:", gc_percent

