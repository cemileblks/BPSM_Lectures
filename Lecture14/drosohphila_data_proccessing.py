#!/usr/bin/python3

# Copy the text file called data.csv from the directory /localdisk/data/BPSM/Lecture14/ to your area.
# The file contains some made-up data for a number of genes.
# Each line contains the following fields for a single gene in this order: species name, sequence, gene name, expression level.
# The fields are separated by commas (hence the "csv" suffix on the filename: csv stands for Comma Separated Values)


# You need to write a Python programme/script that can:
# Print out the gene names for all genes from the species Drosophila melanogaster or Drosophila simulans.
# Print out the gene names for all genes that are between 90 and 110 bases long.
# Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200.
# Print out the gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster.
# For each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65).


# Function to calculate AT content
def at_content(gene):
    gene = str(gene).upper()
    at_count = gene.count("A") + gene.count("T")
    at_content = at_count/len(gene)
    return(at_content)

with open('data.csv') as data_file:
    data_file = data_file.readlines()
    # 1. Gene names for all genes from Drosophila melanogaster or Drosophila simulans
    # split out each line to it's own list with all the info about the gene
    print('Gene names for all genes from the species Drosophila melanogaster or Drosophila simulans:')
    for line in data_file:
        gene_info = line.rstrip('\n').split(',')
        specie = gene_info[0]
        if 'melanogaster' in specie or 'simulans' in specie:
            print(f'\t {gene_info[2]}')

    # 2. Gene names for all genes that are between 90 and 110 bases long
    print('Gene names for all genes that are between 90 and 110 bases long:')
    for line in data_file:
        gene_info = line.rstrip('\n').split(',')
        gene_length = len(gene_info[1])
        if gene_length >= 90 and gene_length <= 110:
            print(f'\t {gene_info[2]}')

    # 3. Gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200
    print(f'Gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200:')
    for line in data_file:
        gene_info = line.rstrip('\n').split(',')
        gene_expression = int(gene_info[3])
        at = at_content(str(gene_info[1]))
        if gene_expression > 200 and at < 0.5:
            print(f'\t{gene_info[2]}')

    # 4. Gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster
    print('Gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster.')
    for line in data_file:
        gene_info = line.rstrip('\n').split(',')
        specie = gene_info[0]
        gene_name = gene_info[2].lower()
        if (gene_name.startswith('k') or gene_name.startswith('h')) and 'melanogaster' not in specie:
            print(f'\t{gene_info[2]}')

    # 5. For each gene, print a message with the AT content classification
    print('AT content of each gene:')
    for line in data_file:
        gene_info = line.rstrip('\n').split(',')
        specie = gene_info[0]
        sequence = str(gene_info[1])
        gene_name = gene_info[2].lower()
        at = at_content(sequence)
        if at > 0.65:
            print(f'AT content is HIGH for {gene_name} gene from {specie}')
        if at < 0.45:
            print(f'AT content is LOW for {gene_name} gene from {specie}')
        if at >= 0.45 and at <= 0.65:
            print(f'AT content MEDIUM for {gene_name} gene from {specie}')
