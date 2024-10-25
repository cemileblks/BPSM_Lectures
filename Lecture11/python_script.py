#!/usr/bin/python3

dna_sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

length_dna = len(dna_sequence)

print("Length of your DNA sequence is", length_dna)

a_nucleotides = dna_sequence.count('A')

print("The number of A nucleotides in  your DNA sequence is", a_nucleotides)

t_nucleotides = dna_sequence.count('T')

print("The number of T nucleotides in  your DNA sequence is", t_nucleotides)

# Ratio of AT to rest of the sequence

at_ratio = (a_nucleotides + t_nucleotides)/ length_dna

print("The ratio of A and T nucleotides to the rest of the dna sequence is", at_ratio)
