import sys

try:
    filename = sys.argv[1]
    with open(filename, "r") as f:
        line_num = 0
        for line in f:
            line = line.rstrip()
            line_num += 1
            print(line_num, ":", len(line))

except IndexError:
    print("Please supply a filename")
except IOError:
    print("I can't read the file:", filename)
