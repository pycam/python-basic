# Write a script that reads a file containing many lines of nucleotide sequence
# For each line in the file, print out the line number,
# the length of the sequence and the sequence

with open('data/dna.txt', "r") as f:
    for line_num, line in enumerate(f, start=1):
        line = line.rstrip()
        print(line_num, "\t", len(line), "\t", line)
