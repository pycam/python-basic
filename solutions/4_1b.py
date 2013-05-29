import sys

try:
    filename = sys.argv[1]
    dna_file = open(filename, "r")
except IndexError:
    print "Please supply a filename"
    sys.exit(0)
except IOError:
    print "I can't read the file:", filename
    sys.exit(0)

line_num = 0

for line in dna_file:
    line = line.rstrip()
    line_num += 1
    print line_num, ":", len(line)

dna_file.close()

    
