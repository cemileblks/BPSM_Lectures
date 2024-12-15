#!/usr/bin/python3

# Write a Python programme/script that will take any DNA sequence and translate it into protein using the translation table.
# What happens if the DNA sequence contains undetermined bases (e.g. N)?
# Can you generate a translation in all three "forward" frames (transcription is on the top strand, starting at base 1, 2, and 3)?
# Can you generate a translation in all three "reverse" frames (transcription is on the bottom strand, starting at base end, end-1, and end-2)?

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

complements = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
}

# Funtion to get the reverse complementary strand
def reverse_complement(dna):
    dna = dna.upper()
    complement_strand = []
    for base in dna:
        if base in complements.keys():
            complement_strand.append(complements[base])
        else:
            return 'Not a valid DNA strand'
    complement_strand.reverse()
    complement_strand = ''.join(complement_strand)
    return complement_strand
            
print(reverse_complement('ATGTTCGGT'))


def dna_translation(dna, reverse_frames = False):
    dna = dna.upper()
    reverse = ''

    # Get the reverse complement if reverse_frames = True
    if reverse_frames == True:
        dna = reverse_complement(dna)
        reverse = '_reverse'
    
    # Create a dictionary to store starting bases for each start position
    translations = {}

    for frame in range(3):
        # Create a list to store each amio acid match
        protein_sequence = []

        # starting positions of each of the strands
        # -3 + 1 to prevent smaller fragements
        start_positions = list(range(frame, (len(dna) - 3 + 1), 3))
        for j in start_positions:
            codon = str(dna[j:j + 3])
            if codon in gencode.keys():
                amino_acid = gencode[codon]
            else: 
                amino_acid = 'X'
            protein_sequence.append(amino_acid)
        
        # Join the list to a string to get the amino acid string
        translated_sequence = ''.join(protein_sequence)
        # Append the sequence start postion with the translated sequence
        translations[f'base{frame + 1}_start{reverse}'] = translated_sequence

    return(translations)

result = dna_translation("ATGTTCGGT")
print(result)

print(dna_translation("ATGTTCGGT", reverse_frames=True))

print(dna_translation("OMGISTHISDNA"))
print(dna_translation("ATGTTCGTGACGAGGGT"))

