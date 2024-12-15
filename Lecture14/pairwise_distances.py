#!/usr/bin/python3

# Pairwise distances: how similar are two sequences?
# Here is a list of DNA sequences that are all equal in length, with varying degrees of similarity to each other:

# ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

# Write a programme/script that calculates and prints, for each pair of sequences, the percentage of identical positions (e.g. base #4 in seq 1 is the same as base #4 in seq 4, and so on).


dna_list = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

# Iterate over each pair of sequences
for i in range(len(dna_list)):
    for j in range(i + 1, len(dna_list)): # to avoid comparing the same pair twice
        seq1 = dna_list[i]
        seq2 = dna_list[j]

        matching_positions = 0
        total_positions = len(seq1)

        # Compare each pase in the sequences
        for pos in range(total_positions):
            if seq1[pos] == seq2[pos]:
                matching_positions +=1
        
        percentage_idential = (matching_positions/total_positions) * 100

        print(f'Sequence {i + 1} vs sequence {j+1}: {percentage_idential:.1f}% identical positions')


# plan
# iterate over each pair of sequences in the list
# compare bases of each position
# calculate percentage
