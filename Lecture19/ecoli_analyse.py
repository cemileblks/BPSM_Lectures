#!/usr/bin/python3

# Using the working code from the Exercise 1, write a script that 
# calls a function that you have written to do the processing. 
# The default sequence should be the ecoli one we used for the 
# lecture. The user should be able to provide the window size, 
# whether they want AT content or GC content plotted, and what 
# portion (base range) of the genome they want analysed

import matplotlib.pyplot as plt


ecoli = open("ecoli.txt").read().replace('\n', '').upper()

window_input = int(input("What window size would you like to be alaysed? please give integer values. e.g. 1000\n\t"))
if window_input > len(ecoli):
    print("Window size entered is greater than E.coli genome, please enter another value")
if window_input <=0:
    print("Please provide a larger input window to proceed")

content_input = input("Would you like AT or GC content analysed?\n\t")
genome_portion_input = input("What portion of teh genome would you liek to be analysed? Pleaes provide ans in list format e.g. [0, 10000]\n\t")
print(genome_portion_input.strip('[]').split(','))
genome_portion_input = genome_portion_input.strip('[]').split(',')

try:
    genome_portion = [int(x) for x in genome_portion_input]
    if len(genome_portion) != 2:
        raise ValueError("The genome portion must contain exactly two elements (start and end indices).")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

def ecoli_genome_processing(window, content, genome_portion):
    window = window_input
    content = content_input
    genome_portion = genome_portion_input

    ecoli_len = ecoli[int(genome_portion[0]):int(genome_portion[1])]

    at = []
    gc = []

    for start in range(len(ecoli_len) - window):
        win = ecoli_len[start:start+window]
        if content == "AT" or content == "TA":
            content = "AT"
            counts = (win.count('A') + win.count('T')) / window
            at.append(counts)

        if content == "GC" or content == "CG":
            content = "GC"
            counts = (win.count('C') + win.count('G')) / window
            gc.append(counts)

    plt.figure(figsize=(20,10))
    if content == "AT":
        plt.plot(at, label="AT")
    if content == "GC":
        plt.plot(gc, label="GC", color = "y")

    plt.ylabel(f'Fraction of {content} content')
    plt.xlabel('Position on genome')
    plt.suptitle(f"{content} content in the E coli genome from {genome_portion[0]} to {genome_portion[1]} bases",fontsize=20) 
    plt.title("Window size of "+str(window),fontsize=14)
    plt.legend()

    plt.savefig(f"Ecoli_{content}.png",transparent=False)

    plt.show()
    plt.close()

ecoli_genome_processing(window_input, content_input, genome_portion_input)