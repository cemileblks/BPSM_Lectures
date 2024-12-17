#!/usr/bin/python3

# Biopython has objects to represent sequences which can do common tasks
import os
from Bio.Seq import Seq
from Bio import SeqIO

my_sequence = Seq("gcgctgattagcggcattgtgattaacggcacccatgaaaccgcgctgaaatga").upper()

my_sequence_cem = Seq("TGTGAGATGATATTAGAG")
(my_sequence_cem.translate(to_stop=True)) # Suprise

print(my_sequence)

# -----------------

# with open("sequences.fasta") as sequence_file:
#     my_fastafile = sequence_file.read()

records = SeqIO.parse("sequences.fasta", "fasta")
print(records)

for seq_record in records:
    print(seq_record)
    print(f"seqrecord ID: {seq_record.id}")
    print(f"\tTranslated protein seq: {seq_record.seq.translate()}")


ids_dict = SeqIO.to_dict(SeqIO.parse("sequences.fasta", "fasta"))
print(ids_dict)
# ids_dict = {
#     'ABC123': SeqRecord(seq=Seq('ATCGTACGATCGATCGATCGCTAGACGTATCG'), 
#                         id='ABC123', 
#                         name='ABC123', 
#                         description='ABC123', 
#                         dbxrefs=[]),
    
#     'DEF456': SeqRecord(seq=Seq('ACTGATCGACGATCGATCGATCACGACT'), 
#                         id='DEF456', 
#                         name='DEF456', 
#                         description='DEF456', 
#                         dbxrefs=[]),
    
#     'HIJ789': SeqRecord(seq=Seq('ACTGACACTGTACTGTACATGTG'), 
#                         id='HIJ789', 
#                         name='HIJ789', 
#                         description='HIJ789', 
#                         dbxrefs=[])
# }