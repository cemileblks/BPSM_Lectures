#!/usr/bin/python3

# Write a Python function that will take a DNA sequence along with an optional threshold and return True or False to indicate whether the DNA sequence contains a high proportion of undetermined bases (i.e not A, T, G or C).
# Write some assertions to test whether the function works.

def undetermined_bases(dna, treshold=10):
    dna = str(dna).upper()
    dna_length = len(dna)
    good_bases_count = dna.count("A") + dna.count("T") + dna.count("C") + dna.count("G")
    bad_bases = dna_length - good_bases_count
    percent_bad_bases = round(bad_bases/dna_length * 100)
    if percent_bad_bases <= 10:
        print(f"Undetermined bases proportion less than treshold {treshold}%, function returns FALSE")
        return False
    else:
        print(f"Undetermined bases proportion more than treshold {treshold}%, function returns TRUE")
        return True
    
assert undetermined_bases('ATGCNNNNNN', 10) == True  # Should return True, >10% undetermined
assert undetermined_bases('ATGCATGC', 10) == False   # Should return False, no undetermined bases
assert undetermined_bases('AATCGXXGCA', 10) == True  # Should return True, >10% undetermined
assert undetermined_bases('GCTAG', 20) == False      # Should return False, no undetermined bases, <20%

# Better solution

def has_high_undetermined_bases(dna_sequence, threshold=10):
    valid_bases = {'A', 'T', 'G', 'C'}
    
    # Count undetermined bases
    undetermined_bases = sum(1 for base in dna_sequence if base not in valid_bases)
    
    # Calculate the percentage of undetermined bases
    undetermined_percentage = (undetermined_bases / len(dna_sequence)) * 100
    
    # Return True if the undetermined percentage is greater than the threshold
    return undetermined_percentage > threshold
