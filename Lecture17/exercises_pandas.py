#!/usr/bin/python3

# Use a pandas dataframe to address the following questions:
# how many fungal species have genomes bigger than 100Mb? What are their names?
# how many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?
# which Heliconius species genomes have been sequenced?
# which sequencing centre has sequenced the most plant genomes? the most insect genomes?
# add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?

import os
import subprocess
import pandas as pd

# Get the file for the data frame if it doesn't exist
if not os.path.exists('eukaryotes.txt'):
    subprocess.call('wget -qO eukaryotes.txt "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt" ' , shell=True)

# Load the data into a DF
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])

# ----------------------------------------------------------------
# Question 1: Fungal species with genomes larger than 100Mb
# Create a new index which is made up of the species name and the accession number
df.index=df.apply(lambda x : "{} ({})".format(x['#Organism/Name'], x['BioSample Accession']), axis=1)

criteria = (df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)

number_of_species = len(df[criteria])

print(f"\n1. Number of fungal species that have genomes bigger than 100Mb: {number_of_species}") # 218
print(f"\n{'-'*80}\n")

# ----------------------------------------------------------------
# Question 2: Number of species sequenced per kingdom/group 
criteria_plants = df['Group'] == 'Plants'
criteria_animals = df['Group'] == 'Animals'
criteria_fungi = df['Group'] == 'Fungi'
criteria_protists = df['Group'] == 'Protists'

number_of_plants = len(df[criteria_plants])
number_of_animals = len(df[criteria_animals])
number_of_fungi = len(df[criteria_fungi])
number_of_protists = len(df[criteria_protists])

print(f"2. Number of species sequenced per kingdom/group:")
print(f"   - Plants:   {number_of_plants}")
print(f"   - Animals:  {number_of_animals}")
print(f"   - Fungi:    {number_of_fungi}")
print(f"   - Protists: {number_of_protists}")
print(f"\n{'-'*80}")

# ----------------------------------------------------------------
# Question 3: Heliconius species genomes
criteria_heliconius = df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'), axis=1)

heliconius = df[criteria_heliconius] # 182 rows

sorted_hel = heliconius.sort_values('#Organism/Name').drop_duplicates(subset='#Organism/Name') # 70 rows, could also use drop duplicates only
number_of_heliconius = len(sorted_hel)

hel_list = list(sorted_hel.loc[:,"#Organism/Name"])

print(f"\n3. Which Heliconius species genomes have been sequenced?")
print(f"There are {number_of_heliconius} Heliconius species genomes that have been sequenced:\n")
print(f"{hel_list}")
print(f"\n{'-'*80}")

# ----------------------------------------------------------------
# Question 4: Sequencing centres with most plant and insect genomes
plant_centre_sorted = df[criteria_plants]['Center'].value_counts()
most_common_center_p = plant_centre_sorted.index[0]

criteria_insects = df['SubGroup'] == 'Insects'

plant_center_sorted = df[criteria_insects]['Center'].value_counts()
most_common_center_i = plant_center_sorted.index[0]

print(f"\n4. Which sequencing centre has sequenced the most plant genomes? the most insect genomes?")
print(f"The center with the most sequenced plants is: {most_common_center_p}")
print(f"The center with the most sequenced insects is: {most_common_center_i}")
print(f"\n{'-'*80}")

# ----------------------------------------------------------------
# Question 5: Proteins per gene and genomes with at least 10% more proteins than genes
df['ProteinsPerGene'] = df.apply(lambda x : x['Proteins']/x['Genes'], axis=1)

criteria_more_proteins = ((df['Proteins'] - df['Genes'])/df['Genes'] * 100) > 10

df_more_proteins = df[criteria_more_proteins] # 1070

genomes_more_proteins = list(df_more_proteins.loc[:,'#Organism/Name'])

print(f"\n4. Which genomes have at least 10% more proteins than genes?")
print(f"Number of genomes with at least 10% more proteins than genes: {len(df_more_proteins)}")

user_input = input("Would you like to see the full list of species? (yes/no): ").strip().lower()

if user_input == 'yes':
    print(f"These genomes belong to the following species: {', '.join(genomes_more_proteins)}")
else:
    print("You chose not to display the full list.")