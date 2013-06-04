def count_gs_and_cs(sequence):

  return sequence.count( "G" ) + sequence.count( "C" )


def is_valid_dna(sequence):

  return set( "ATGC" ).issuperset( sequence )


import sys

if len( sys.argv ) != 2:
  print "Usage: %s sequence" % sys.argv[0]
  sys.exit( 1 )

sequence = sys.argv[1].upper()

if not is_valid_dna( sequence ):
  print "Invalid characters in sequence"
  sys.exit( 1 )

print count_gs_and_cs( sequence=sequence )


