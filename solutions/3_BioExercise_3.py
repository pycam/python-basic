gesScale = {'F': -3.7, 'M': -3.4, 'I': -3.1, 'L': -2.8, 'V': -2.6,
'C': -2.0, 'W': -1.9, 'A': -1.6, 'T': -1.2, 'G': -1.0, 'S': -0.6,
'P': 0.2, 'Y': 0.7, 'H': 3.0, 'Q': 4.1, 'N': 4.8, 'E': 8.2,
'K': 8.8, 'D': 9.2, 'R': 12.3}


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


def hydrophobicity_search(seq, scale, winSize=15):
    """Scan a protein sequence for hydrophobic regions using the GES
    hydrophobicity scale."""

    subSeqs = calculate_windows(seq, winSize)
    scoreList = []
    for sequence in subSeqs:
        values = [scale[aa] for aa in sequence]
        score = sum(values)
        scoreList.append(score)
    return scoreList

proteinSeq = 'IRTNGTHMQPLLKLMKFQKFLLELFTLQKRKPEKGYNLPIISLNQ'
scores = hydrophobicity_search(proteinSeq, gesScale)
print scores

#Requires matplotlib to be installed
from matplotlib import pyplot
pyplot.plot(scores)
pyplot.show()