def pretty_print(seq, separator="-", group = 3):
  
  if len( seq ) % group != 0:
    raise ValueError( "Sequence length not divisable by %s" % group )

  frags = []

  for start in range( 0, len( seq ), group ):
    frags.append( seq[start:start+group] )

  return separator.join( frags )


if __name__ == "__main__":
  dna = "ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG"
  print dna
  print pretty_print( dna )

  bad = "ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGT"
  print bad
  print pretty_print( bad )
