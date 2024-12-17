#!/usr/bin/python3

# Let's look at the base composition in kilobase sliding windows along the first 100kb of the E. coli genome, 
# stored as a plain text file called ecoli.txt

import os, sys
import numpy as np
import matplotlib.pyplot as plt

# Open the file, read it, and remove the newlines to get one long string
# then take the first 100000 characters
ecoli = open("ecoli.txt").read().replace('\n', '').upper()[0:100000]

# Set sliding window size
window = 1000

# Four lists to hold the numbers of each base
a = []
t = []
g = []
c = []

# iterate over all the starting positions
for start in range(len(ecoli) - window):
    # get the current sliding window
    win = ecoli[start:start+window]
    # count each of the four bases and append to the list
    a.append(win.count('A') / window)
    t.append(win.count('T') / window)
    g.append(win.count('G') / window)
    c.append(win.count('C') / window)

# Plot the lists with appropriate labels
plt.figure(figsize=(20,10))
plt.plot(a, label="A")
plt.plot(t, label="T")
plt.plot(g, label="G")
plt.plot(c, label="C")
plt.ylabel('Fraction of bases')
plt.xlabel('Position on genome')
plt.legend()

plt.savefig("Chart_15.png",transparent=False)

plt.show()
plt.close()
# ----------------------------------

# By changing the code just a little bit, we can plot something else e.g. the fraction of repeated dinucleotides, one panel per base.

# Four lists to hold the numbers of each dinucleotide
aa = []
tt = []
gg = []
cc = []

# Iterate over all the starting positions
counter =0
for start in range(len(ecoli) - window):
# Get the current sliding window
    counter += 1
    # print(counter)
    win = ecoli[start:start+window]
# Count each of the four bases and append to the list
    aa.append(win.count('AA') / win.count('A'))
    tt.append(win.count('TT') / win.count('T'))
    gg.append(win.count('GG') / win.count('G'))
    cc.append(win.count('CC') / win.count('C'))
    

# Plot the lists with appropriate labels
plt.figure(figsize=(20,10))

# First panel
plt.subplot(221)
plt.plot(aa, label="AA rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()

# Second panel
plt.subplot(222)
plt.plot(tt, label="TT rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()

# Third panel
plt.subplot(223)
plt.plot(gg, label="GG rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()

# Fourth panel
plt.subplot(224)
plt.plot(cc, label="CC rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()

# Save and show
plt.savefig("Chart_16.png",transparent=False)
plt.show()
plt.close()

# --------------------------------------------

# Or we can change the sliding window size, e.g. to 10000
# Four lists to hold the numbers of each nucleotide
a = []
t = []
g = []
c = []

# Iterate over all the starting positions
for start in range(len(ecoli) - window):
    win = ecoli[start:start+window]
    a.append(win.count('A') / window)
    t.append(win.count('T') / window)
    g.append(win.count('G') / window)
    c.append(win.count('C') / window)


# Do the plotting bits
# Python "responses" not shown
plt.figure(figsize=(20,10))
plt.plot(a, label="A",linewidth=3)
plt.plot(t, label="T",linewidth=3)
plt.plot(g, label="G",linewidth=3)
plt.plot(c, label="C",linewidth=3)
plt.ylabel('Fraction of bases')
plt.xlabel('Position on genome')
plt.suptitle("Base composition in the E coli genome",fontsize=20) # Note!
plt.title("Window size of "+str(window),fontsize=14)
plt.legend()
plt.savefig("Chart_16A.png",transparent=False)
plt.show()
plt.close()