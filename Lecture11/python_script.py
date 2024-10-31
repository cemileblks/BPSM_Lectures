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

# Complementing DNA

print("The complement sequence of your DNA sequence is:", dna_sequence.replace('A','t').replace('T','a').replace('C','g').replace('G','c').upper())

# Restriction fragment Lengths

dna_sequence2 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

cut_regions = dna_sequence2.count("GAATTC")

print("number of cut_regions", cut_regions)

motif_position = dna_sequence2.find("GAATTC")

print("The position of the cut_region is", motif_position)

frag1_length = dna_sequence2.find("GAATTC") + 1

frag2_length = len(dna_sequence2) - frag1_length

print("Length of fragment one is " + str(frag1_length))
print("Length of fragment two is " + str(frag2_length))

# Splicing out introns

genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1 = genomic_dna[0:63]

exon2 = genomic_dna[90:]

coding_seq = exon1 + exon2

print("\nyour coding sequence is", coding_seq)

# calculate what percentage of the DNA sequence is coding

coding_length = len(coding_seq)

percent_coding = coding_length/len(genomic_dna) *100

print(str(int(percent_coding))+ "% percent of the DNA sequence is coding")

# uppercase exon lowercase intron

intron = genomic_dna[63:90].lower()

sequence = exon1 + intron + exon2

print("your sequence is " + sequence)

print("TEST", len(genomic_dna), len(sequence))
