import sys

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
except IndexError:
    print "Please supply 2 command line arguments"
    sys.exit(0)
except ValueError:
    print "Please supply 2 integers"
    sys.exit(0)

sum = x + y

print "Sum of %d and %d: %d" % (x, y, sum)

