def flatten(seq):

  result = []

  for elem in seq:
    try:
      length = len( elem )

    except TypeError: # not a list
      result.append( elem )

    else:
      result.extend( flatten( elem ) )

  return result

if __name__ == "__main__":
  seq = [ ( 1, 2, 3 ), ( 4, ( 5, 6 ) ) ]
  print flatten( seq )
