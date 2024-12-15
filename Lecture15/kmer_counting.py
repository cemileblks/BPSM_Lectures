#!/usr/bin/python3

# Write a Python function that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than n times.

# Write a Python script/programme that, given any DNA sequence, will print a list of k-mers that occur more than some number of times.

# The user should be asked to supply, on the command line, the following:
# the sequence of interest
# the kmer length for analysis
# the threshold frequency of kmers found (i.e. the "more than this number" value)

try:
    sequence_user_input = input('Enter your sequence please: ')

    # Validate sequence length
    if len(sequence_user_input) == 0:
        raise ValueError('Sequence cannot be empty.')

    kmer_size = int(input('What is your choice for the size of k-mers? '))

    # Ensure kmer size is less than or equal to sequence length
    if kmer_size > len(sequence_user_input):
        raise ValueError('Kmer size cannot be greater than the length of the sequence.')

    frequency = int(input('What is your choice for threshold frequency of k-mers to look for?'))

except ValueError as e:
    print(f'Error: {e}. Please enter valid inputs.')

def kmer_counts(sequence, kmersize = 2, minfrequency = 2):
    sequence = str(sequence).upper()

    kmersize = int(kmersize)
    minfrequency = int(minfrequency)

    kmers = {}

    for i in range(len(sequence) - kmersize + 1):
        kmer = sequence[i:i+kmersize]

        if kmer in kmers:
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1


    print(f"K-mers of length {kmersize}, that occur more than {minfrequency} times are:")
    for item in kmers.items():
        if item[1] > minfrequency:
            print(f'{item[0]}, occured {item[1]} times')






kmer_counts(sequence_user_input, kmer_size, frequency)