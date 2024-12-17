#!/usr/bin/python3

# Use the ecoli.txt file and, using the code above as a starting point, make a chart which shows the AT content in a sliding 1000 base window
# for the first 50000 bases
# for the first 100000 bases
# for the whole genome

import matplotlib.pyplot as plt

ecoli = open("ecoli.txt").read().replace('\n', '').upper()

window = 1000

ecoli_len = ecoli[:50000]

at = []

for start in range(len(ecoli_len) - window):
    win = ecoli_len[start:start+window]
    counts = (win.count('A') + win.count('T')) / window
    at.append(counts)

plt.figure(figsize=(20,10))
plt.plot(at, label="AT")

plt.ylabel('Fraction of AT content')
plt.xlabel('Position on genome')
plt.suptitle(f"AT content in the E coli genome for the first {len(ecoli_len)} bases",fontsize=20) 
plt.title("Window size of "+str(window),fontsize=14)
plt.legend()


plt.savefig("Exercise1_fig1.png",transparent=False)

plt.show()
plt.close()

# ------------------------------------------------------------

ecoli_len = ecoli[:100000]
at = []

for start in range(len(ecoli_len) - window):
    win = ecoli_len[start:start+window]
    counts = (win.count('A') + win.count('T')) / window
    at.append(counts)

plt.figure(figsize=(20,10))
plt.plot(at, label="AT")

plt.ylabel('Fraction of AT content')
plt.xlabel('Position on genome')
plt.suptitle(f"AT content in the E coli genome for the first {len(ecoli_len)} bases",fontsize=20) 
plt.title("Window size of "+str(window),fontsize=14)
plt.legend()


plt.savefig("Exercise1_fig2.png",transparent=False)

plt.show()
plt.close()

# -------------------------------------------

ecoli_len = ecoli
at = []

for start in range(len(ecoli_len) - window):
    win = ecoli_len[start:start+window]
    counts = (win.count('A') + win.count('T')) / window
    at.append(counts)

plt.figure(figsize=(20,10))
plt.plot(at, label="AT")

plt.ylabel('Fraction of AT content')
plt.xlabel('Position on genome')
plt.suptitle(f"AT content in the E coli genome",fontsize=20) 
plt.title("Window size of "+str(window),fontsize=14)
plt.legend()


plt.savefig("Exercise1_fig3.png",transparent=False)

plt.show()
plt.close()
