#!/usr/bin/python
import sys

input_file = sys.stdin

if len(sys.argv) > 1:
    try:
        input_file = open(sys.argv[1], "r")
    except IOError:
        print "I can't open:", sys.argv[1]
        sys.exit(0)

for line in input_file:
    sys.stdout.write(line)

