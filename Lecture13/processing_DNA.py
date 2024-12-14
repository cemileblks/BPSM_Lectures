#!/usr/bin/python3

# The file input.txt contains a number of DNA sequences, one per line.
# Each sequence starts with the same 14 base pairs : these are from a sequencing adapter that should have been removed.

# Write a Python script/programme that will :
# (a) trim the adapter and write the 'cleaned' (adapter-free) sequences to a single new file AND
# (b) print the length of each adapter-free sequence to the screen.


print("Processing DNA file in input.txt...\nTrimming the adapter sequences from each line, and writing them to a new file called Cleaned_sequences.txt\n\n")

with open('input.txt', 'r') as input_file, open('Cleaned_sequences.txt', 'w') as cleanseqs: 
    for line in input_file:
        cleaned_line = line[14:].strip()
        cleanseqs.write(cleaned_line + '\n')
        lenght_of_seq = str(len(cleaned_line))
        print('Lengh of the adapter-free sequence is ' + lenght_of_seq + '\nthe sequence is:\n' + cleaned_line)
