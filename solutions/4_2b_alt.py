import sys

for line in sys.stdin:
    line = line.rstrip()
    pop, sample_id, sample_name, sex = line.split(",")
    if (sample_id == sys.argv[1]):
        print "Found", sample_id
        break

else:
    print 'Not found'

