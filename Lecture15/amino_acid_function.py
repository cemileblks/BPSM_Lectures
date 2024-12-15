#!/usr/bin/python3

# Write a Python function that takes two arguments (a protein sequence and an amino acid residue code) and returns the percentage of the protein that the amino acid makes up.

# Modify the function from the previous exercise above so that it accepts a list of amino acid residues rather than a single one, and count these within the protein sequence.
# If no list is given, the function should return the percentage of hydrophobic amino acid residues (i.e. amino acids A, I, L, M, F, W, Y, V).

def amino_acid_percentage(protein_seq, amino_acid_list = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    protein_seq = str(protein_seq).upper()
    amino_count = 0
    for amino_acid in amino_acid_list:
        amino_acid = str(amino_acid).upper()
        amino_count += protein_seq.count(amino_acid)
    amino_percentage = round((amino_count/len(protein_seq)) * 100)
    return amino_percentage

# Assert statements for exercise 1
assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
# Assert statements for exercise 2
assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP")) == 65