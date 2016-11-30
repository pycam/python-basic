from ex2_2_2 import gc_content
from ex2_2_3 import extract_sub_sequences


def gc_content_along_the_chain(dna_sequence, window_size):
    """Returns a list of GC along the DNA sequence
    given a DNA sequence and the size of the sliding window
    """
    sub_sequences = extract_sub_sequences(dna_sequence, window_size)
    gc_results = []
    for sub_sequence in sub_sequences:
        gc_results.append(gc_content(sub_sequence))
    return gc_results

dna = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
print(gc_content(dna))
print(extract_sub_sequences(dna, 5))
print(gc_content_along_the_chain(dna, 5))
