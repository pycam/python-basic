def extract_sub_sequences(sequence, window_size):
    """Extract a list of overlaping sub-sequences for a given window size
    from a given sequence.
    """
    if window_size <= 0:
        return "Window size must be a positive integer"
    if window_size > len(sequence):
        return "Window size is larger than sequence length"
    result = []
    nr_windows = len(sequence) - window_size + 1
    for i in range(nr_windows):
        sub_sequence = sequence[i:i + window_size]
        result.append(sub_sequence)
    return result


#dna = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
#print(extract_sub_sequences(dna, 5))
