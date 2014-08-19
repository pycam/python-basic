def calculate_windows(seq, winSize): 
	if winSize <= 0:
		raise Exception("Window size must be a positive integer")
	if winSize > len(seq):
		raise Exception("Window size is larger than sequence length")
	result = []
	nrWindows = len(seq)-winSize+1
	for i in range(nrWindows):
		subSeq = seq[i:i+winSize]
		result.append(subSeq)
	return result
    
def calcGcContent(seq, winSize=10): 
	subSeqs = calculate_windows(seq, winSize)
	gcValues = []
	for sequence in subSeqs:
		numGc = sequence.count('G') + sequence.count('C')
		value = numGc/float(winSize) # at least in Python 2.4, 2.5 
		gcValues.append(value)
	return gcValues

dnaSeq = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
gcResults = calcGcContent( dnaSeq )
print gcResults

#Requires matplotlib to be installed
#from matplotlib import pyplot
#pyplot.plot( gcResults )
#pyplot.show()