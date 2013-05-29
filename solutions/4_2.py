import sys

try:
    filename = sys.argv[1]
    dna_file = open(filename, "r")
except IndexError:
    print "Please supply a filename"
    exit(0)
except IOError:
    print "I can't read the file:", filename
    exit(0)

for line_num, line in enumerate(dna_file):
    print "%d: %d" % (line_num, len(line))

dna_file.close()

    
