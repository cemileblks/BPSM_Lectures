#!/usr/bin/python3

# In the directory
# /localdisk/data/BPSM/Lecture13/
# is a collection of files whose names end in .dna.
# Each file holds a collection of DNA sequences, one per line.
# What is required:
# Write a Python script/programme which creates nine new 'size range' directories, one for sequences between 100 and 199 bases long, one for sequences between 200 and 299 bases long, etc., etc..
# Choose one of the .dna files as an input file, and write out each DNA sequence in that input file to a separate file in the appropriate 'size range' directory.

import os, sys, subprocess, shutil

# Variable for arbitary seq id number
seq_number = 1

for file_name in sorted(os.listdir('dna_files')):
    # check if the file name ends with dna
    if file_name.endswith('.dna'):
        print(f'Reading sequences from {file_name}')
        # Open file and process each line
        dna_file = open(f'dna_files/{file_name}')
        # Calculate the sequence length
        for line in dna_file:
            dna = line.rstrip('\n')
            length = len(dna)
            print(f'\tSequence length is {length}')
            # Go thorugh each size bin and check if the sequence belongs there
            for bin_lower in list(range(100, 1000, 100)):
                bin_upper = bin_lower + 99

                if length >= bin_lower and length <= bin_upper:
                    print(f'\t\tbin is {str(bin_lower)} to {str(bin_upper)}')
                    
                    directory_name = f'{bin_lower}_{bin_upper}'
                    # make directory if it does't exist for the smaller dna files
                    if os.path.exists(directory_name) == False:
                        os.mkdir(directory_name)
                    
                    output_path = directory_name + '/' + str(seq_number)+ '.dna'
                    output = open(output_path, 'w')
                    output.write(dna)
                    output.close()
                    # increment the sequence number
                    seq_number +=1


# shutil.rmtree(directory_name) # to remove the directory from previous run of the script
