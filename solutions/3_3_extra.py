def ReverseComplement(seq):
	revdic = {'A':'T','T':'A','G':'C','C':'G'}
	
	seq = seq.upper()
	seq = reversed(seq)
	result = []
	for base in seq:
		#check if seq is a DNA sequence or not
		if base not in 'ATCG':
			raise TypeError("NOT a DNA sequence")
		complement = revdic[base]
		result.append(complement)
	
	result = "".join(result)
	return result
	
	
seq = 'ATCGTAGCatgcAATTGGC'
print ReverseComplement(seq)