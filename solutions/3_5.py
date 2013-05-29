frags = [ "ACTGTGT", "TTCTG", "TTA", "GGTGTACAT", "AAAATCTGAAA" ]
print "Before sorting:"
print frags
frags.sort( key = lambda s: s.count( "A" ) )
print "After sorting:"
print frags

