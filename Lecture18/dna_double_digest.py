#!/usr/bin/python3

# A file called long_dna.txt has been put in the following directory:
# /localdisk/data/BPSM/Lecture18

# It contains a made-up DNA sequence.
# What fragment lengths will we get if we digest the sequence with a novel restriction enzyme BpsmI, whose recognition site is ANT*AAT, where * indicates the position of the cut site.
# What will the fragment lengths be if we do a double digest with both BpsmI and BpsmII (whose recognition site is GCRW*TG)?
# What are the sequences of the fragments themselves?

import re

with open('long_dna.txt') as dna_file:
    dna = dna_file.read().rstrip('\n')
    print(len(dna))
    

BpsmI = r"A.TAAT"
restriction_sites = re.finditer(BpsmI, dna)

fragment_start = 0
count = 0
fragments = []
for site in restriction_sites:
    count += 1
    recognition_site = site.start()

    fragment = dna[fragment_start:recognition_site+3]

    fragments.append(fragment)

    print(f'BpsmI Fragment {count}:')
    print(f'Recognition site found at position {site.span()}.')
    print(f'The position of the cut is at literal position {site.start()+3}.')
    print(f'Length of fragment {count}: {len(fragment)}')
    print(f'Fragment sequence: {fragment}\n')

    fragment_start = recognition_site + len(BpsmI)
    if count == len(list(re.finditer(BpsmI, dna))) :
        count +=1
        fragment_start -= 3
        fragment = dna[fragment_start:]

        print(f'BpsmI Fragment {count}:')
        print(f'Length of fragment {count}: {len(fragment)}')
        print(f'Fragment sequence: {fragment}\n')

print(f'{"-"*80}') # --------------------------------------------------------
# What will the fragment lengths be if we do a double digest with both BpsmI and BpsmII (whose recognition site is GCRW*TG)?
# What are the sequences of the fragments themselves?

# The restriction sites
BpsmI = r"A.TAAT"
BpsmII = r"GC(G|A)(A|T)TG"

restriction_sitesI = re.finditer(BpsmI, dna)
restriction_sitesII = re.finditer(BpsmII, dna)

# list to store all cut positions
all_restriction_cuts = []

for site in restriction_sitesI:
    all_restriction_cuts.append(site.start()+3)

for site in restriction_sitesII:
    all_restriction_cuts.append(site.start()+4)

# Sort from smallest to largest to find the respective cuts in the dna
all_restriction_cuts.sort()

count = 0
fragment_start = 0

# Loop through every cut position
for cut_position in all_restriction_cuts:
    count +=1
    # Fragment lenght is cut position minus the start of the fragment (fragment start equals the previous cut position)
    fragment_length = cut_position - fragment_start
    print(f'Fragment {count} is {fragment_length} bp long. From position {fragment_start} to {cut_position}')
    fragment = dna[fragment_start:cut_position]
    print(f'Fragment sequence: {fragment}\n')

    fragment_start = cut_position

# last fragment that is from last starting pos to the end of the sequence
fragment_length = len(dna) - fragment_start
count += 1
print(f'Fragment {count} is {fragment_length} bp long. From position {fragment_start} to {len(dna)}')
fragment = dna[fragment_start:]
print(f'Fragment sequence: {fragment}\n')
