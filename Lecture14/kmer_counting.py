#!/usr/bin/python3

# K-mers are short DNA subsequences with length "k" bases, and are usually generated using the "sliding window" method we used in the last lecture's exercise.

# Write a programme/script that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than some number of times n (you chose what the number n is!).

# For example, with
# dna="ATGCATCATG"
# k=2 # kmer size
# n=2 # more than this number found

# Sliding window with offset of 1 and with k=2 gives:
# AT
#  TG 
#   GC 
#    CA
#     AT ... and so on

# so the result for this example should be AT because the kmers (k) are 2 bases long, and there are 3 instances of AT (n was 2, and 3 is more than 2).

# Neither CA nor TG get listed: they do appear twice each, but 2 is not more than 2....!


# set kmer size 
# set the number of times you want to check if that kmer is repeated
# use sliding window approach

def find_frequent_kmers(dna_sequence, k, n):
    if len(dna_sequence) < k:
        print("Input sequence is shorter than k-mer length")
        return
    
    kmer_count = {}

    for start_window in range(len(dna_sequence) - k + 1):
        kmer = dna_sequence[start_window:start_window + k]
        if kmer in kmer_count:
            kmer_count[kmer] +=1
        else:
            kmer_count[kmer] = 1

    # Print out the kmers that occur more than n times
    print(f'K-mers that occur more than {n} times in the input sequence are:')
    for kmer, count in kmer_count.items():
        if count > n:
            print(f'{kmer}: {count} times')

my_dna = 'ATGCATCATG'

# Set k-mer size and the threshold n
k = 2
n = 2

find_frequent_kmers(my_dna, k, n)