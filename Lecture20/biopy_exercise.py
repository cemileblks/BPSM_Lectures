#!/usr/bin/python3

from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "cemileb.studies@gmail.com"

api_key = "9d316974fd23bf6c756633a98cfac5831a08"

print(Entrez.einfo())
IO_link = Entrez.einfo()
record = Entrez.read(IO_link)

# print(record)
# print(record.values())

# # How many COX1 Protein records are there for mamals
mysearch = Entrez.esearch(db="protein", term="COX1 Mammalia complete", retmax="20")
result = Entrez.read(mysearch)
print(result)

count = 1
for accession in result['IdList']:
    genbank_file = Entrez.efetch(db="protein", id=accession, rettype="gb")
    record = SeqIO.read(genbank_file, "genbank")
    print("COX1", record.description)
    count +=1
    if count == 6:
        break

# Avg length

# Function

