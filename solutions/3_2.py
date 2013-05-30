def check_sequence1(seq, polymer = "DNA"):

  if polymer =="DNA":
    valids = set( [ "A", "C", "G", "T" ] )

  elif polymer == "RNA":
    valids = set( [ "A", "C", "G", "U" ] )

  for c in seq:
    if c not in valids:
      return False

  return True


def check_sequence2(seq, polymer = "DNA"):

  if polymer =="DNA":
    valids = set( [ "A", "C", "G", "T" ] )

  elif polymer == "RNA":
    valids = set( [ "A", "C", "G", "U" ] )

  return all( [ c in valids for c in seq ] )


if __name__ == "__main__":
  dna = "ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG"
  print "DNA sequence: %s" % dna
  print "Check as DNA, method1: %s" % check_sequence1( seq=dna )
  print "Check as DNA, method2: %s" % check_sequence2( seq=dna )
  print "Check as RNA, method1: %s" % check_sequence1( seq=dna, polymer="RNA" )
  print "Check as RNA, method2: %s" % check_sequence2( seq=dna, polymer="RNA" )

  rna = "AUGGUGCAU"
  print "RNA sequence: %s" % rna
  print "Check as DNA, method1: %s" % check_sequence1( seq=rna )
  print "Check as DNA, method2: %s" % check_sequence2( seq=rna )
  print "Check as RNA, method1: %s" % check_sequence1( seq=rna, polymer="RNA" )
  print "Check as RNA, method2: %s" % check_sequence2( seq=rna, polymer="RNA" )

