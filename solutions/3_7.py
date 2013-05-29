def factorial1(number):

  result = 1

  for value in range( 2, number + 1 ):
    result *= value

  return result


def factorial2(number):

  import operator
  return reduce( operator.mul, range(2, number+1), 1)


if __name__ == "__main__":
  print "factorial1"
  print "4!=%s" % factorial1(4)
  print "6!=%s" % factorial1(6)
  
  print "factorial2"
  print "4!=%s" % factorial2(4)
  print "6!=%s" % factorial2(6)

