from Bio import SeqIO

from Bio.SeqUtils import GC

# Read in a FASTA file named <denv.sample.fa>

seqList = list(SeqIO.parse('data/sample.fa','fasta'))

# find the number of sequences present in the file

numSeq = len(seqList)

print('\nTotal number of sequences:', numSeq)

# find IDs and lengths of the longest and the shortest sequences

maxLen = minLen = len(seqList[0].seq)

lSeq = sSeq = seqList[0].id

for i in range(1,numSeq):
    if len(seqList[i].seq) > maxLen:
        # update maxLen and lSeq
        maxLen = len(seqList[i].seq)
        lSeq = seqList[i].id
        
    elif len(seqList[i].seq) < minLen:
        # update minLen and sSeq
        minLen = len(seqList[i].seq)
        sSeq = seqList[i].id

print('\nLongest sequence is', lSeq, 'with length', maxLen, 'bp')
print('Shortest sequence is', sSeq, 'with length', minLen, 'bp\n')

# Creating a new sequence list containing sequences longer than 500bp
# Calculating the average length of these sequences
# calculate and print the percentage of GC contents

longSeqList = list()  # empty list for sequences

totLength = 0

for sequence in seqList:
    if len(sequence) > 500:
        longSeqList.append(sequence)
        totLength += len(sequence)
        gc = GC(sequence.seq)
        print('Percentage of GC content in', sequence.id, 'is', gc)

avgLength = totLength / len(longSeqList)

print('\nAverage length for sequences longer than 500bp is', avgLength)


# Write sequences in the longSeqList in a file with 'GenBank' format

SeqIO.write(longSeqList,'sample.long.fa','fasta')

