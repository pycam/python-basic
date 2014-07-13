frags = ["ACTGTGT", "TTCTG", "TTA", "GGTGTACAT", "AAAATCTGAAA"]
frags.sort()
print "sorted alphabetically:", frags

frags.sort( key=len )
print "sorted by fragment length:", frags

frags.sort( key=lambda s: s.count('A') )
print "sorted by number of Adenines:", frags
