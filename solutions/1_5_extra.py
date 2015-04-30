seq = "MKALIVLGLVLLSVTVQGKVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTRATNYNAGDRSTDYGIFQINSRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDPQGIRAWVAWRNRCQNRDVRQYVQGCGV"

# unique amino acids in the sequence
unique_aa = set(list(seq))

# sorted amino acids
unique_aa_sorted = sorted(list(unique_aa))
print unique_aa_sorted

# storing the occurences in a dictionary
aa_counts = {}
aa_counts['A'] = seq.count('A')
aa_counts['C'] = seq.count('C')
aa_counts['D'] = seq.count('D')
# etc...

print aa_counts

# printing the results
print 'A has', aa_counts['A'], 'occurrence(s)'
print 'C has', aa_counts['C'], 'occurrence(s)'
print 'D has', aa_counts['D'], 'occurrence(s)'
print "etc..."


# To fully solve this problem, you'll need to learn about loops which are described
# in the next course section

# Add counts one by one to an empty dictionary
aa_counts = {}
for aa in set(seq):
    aa_counts[aa] = seq.count(aa)

# Sort the keys of the dictionary in alphabetic order:
keys = aa_counts.keys()
keys.sort()

# Print the results by key sorted by alphabetic order
for aa in keys:
    print "%s has %i occurrence(s)" % (aa, aa_counts[aa])

