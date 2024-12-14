#!/usr/bin/python3

# The file genomic_dna2.txt contains a section of genomic DNA.
# The file exons.txt contains a list of start/stop positions of exons.
# Each exon is on a separate line and the start and stop positions are separated by a comma.

# Write a Python script/programme that will extract the exon segments, concatenate them, and write them to a new file.


with open('genomic_dna2.txt') as genomic_dna_file, open('exons.txt') as exon_file, open('coding_genomic_dna2.txt', 'w') as coding_genomic_file:
    genomic_dna = genomic_dna_file.read().upper()
    exons_list = exon_file.read().split()
    print(exons_list)
    coding_genomic_dna = []
    count = 0
    for exon in exons_list:
        exon = exon.split(',')
        print(exon)
        startexon = int(exon[0]) - 1
        endexon = int(exon[1])
        count+=1 
        print(f'Exon{count}: This is exon {exon[0]},{exon[1]} runs from index position {startexon} but not including {endexon}')
        print(genomic_dna[startexon:endexon])
        coding_genomic_dna.append(genomic_dna[startexon:endexon])
    coding_genomic_dna = ''.join(coding_genomic_dna)
    print('Length of whole dna sequence was', len(genomic_dna), '\nLength of the coding sequence is', len(coding_genomic_dna), 'and can be found in the file coding_genomic_dna2.txt')
    coding_genomic_file.write(coding_genomic_dna)



# Get the genomic dna from file
# Get the exons form the other file
# Extract each of the exons form the genomic dna file 
# Concantenate them
# Write to a new file 
