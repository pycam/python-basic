def count_and_print_gs(sequence):

  print(sequence.upper().count( "G" ))


import sys

if len( sys.argv ) != 2:
  print("Usage: %s sequence" % sys.argv[0])
  sys.exit( 1 )

count_and_print_gs( sequence=sys.argv[1] )


