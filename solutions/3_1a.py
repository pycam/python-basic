def count_gs_and_cs(sequence):

  return sequence.count( "G" ) + sequence.count( "C" )


import sys

if len( sys.argv ) != 2:
  print "Usage: %s sequence" % sys.argv[0]
  sys.exit( 1 )

print count_gs_and_cs( sequence=sys.argv[1].upper() )


