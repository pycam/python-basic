# 1-letter code lysozyme protein sequence given
seq = "MKALIVLGLVLLSVTVQGKVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTRATNYNAGDRSTDYGIFQINSRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDPQGIRAWVAWRNRCQNRDVRQYVQGCGV"

# Count the abundance of different residue types and store the result in a dictionary
aa_counts = {}
aa_counts['A'] = seq.count('A')
aa_counts['C'] = seq.count('C')
aa_counts['D'] = seq.count('D')
aa_counts['E'] = seq.count('E')
# etc...

# Print the results in alphabetical order
print 'A has', aa_counts['A'], 'occurrence(s)'
print 'C has', aa_counts['C'], 'occurrence(s)'
print 'D has', aa_counts['D'], 'occurrence(s)'
print 'E has', aa_counts['E'], 'occurrence(s)'
