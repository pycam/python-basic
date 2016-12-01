# Write a script that reads a file containing many lines of nucleotide sequence
# For each line in the file, print out the line number,
# the length of the sequence and the sequence

import sys

with open('data/dna.txt', "r") as f:
    line_num = 0
    for line in f:
        line = line.rstrip()
        line_num += 1
        print(line_num, ":", len(line), "\t", line)
