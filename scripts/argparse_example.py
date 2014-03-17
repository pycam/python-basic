# an example of using the argparse library to parse command line arguments

import argparse

def gc_content(seq):
    seq = seq.upper()
    return (seq.count('G') + seq.count('C')) / float(len(seq))

parser = argparse.ArgumentParser(description='GC content calculator')
parser.add_argument('-s', '--seq', help='nucleotide sequence', required=True)
parser.add_argument('-l', '--len', action='store_true', help='compute the length of the sequence')
args = parser.parse_args()

print "GC:", gc_content(args.seq)

if args.len:
    print "length:", len(args.seq)

