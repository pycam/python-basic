bases = ['A', 'T', 'T', 'C', 'G', 'G', 'T', 'C', 'A', 'T', 'G', 'C', 'T', 'A', 'A']

print "All bases:"
for base in bases:
    print base


print "Every 3rd base:"
pos = 2
while pos <= 12:
    print bases[pos]
    pos += 3

