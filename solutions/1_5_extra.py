lysSeq = "MKALIVLGLVLLSVTVQGKVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTRATNYNAGDRSTDYGIFQINSRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDPQGIRAWVAWRNRCQNRDVRQYVQGCGV"

#set(lysSeq)
#set(['A', 'C', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'M', 'L', 'N', 'Q', 'P', 'S', 'R', 'T', 'W', 'V', 'Y']


#Add counts one by one to an empty dictionary
aaCounts = {}
for aa in set(lysSeq):
	aaCounts[aa] = lysSeq.count(aa)

#Sort the keys of the dictionary in alphabetic order:
keys = aaCounts.keys()
keys.sort()

#print the results in the screen by alphabetic key order:
for aa in keys:
	print "%s: %i" %(aa, aaCounts[aa])

