#!/usr/bin/python3

# You need to write a Python script/programme that will generate overlapping short segments from a long string (i.e. a sliding window approach); e.g. if your input sequence was
# abcdefghijk
# and the window size chosen was 6, and the offset was 1, then the segments would be :
# abcdef
# bcdefg
# cdefgh
# defghi
# efghij
# fghijk


# Using the protein-coding region from the AJ223353 NCBI sequence ('remote_exon01.fasta', or whatever you called it) that you generated while doing the exercises in the last lecture, write a Python programme that generates segments that are 30 bases long, with a window offset of 3.
# Modify your Python script/programme to print each sliding window segment to the screen.
# Modify your Python script/programme to print the percentage GC content of each sliding window segment and the sequence.
# Modify your Python script/programme to write out the individual segments in fasta format (i.e. with an informative fasta header) into individual fasta files.
# Modify your Python script/programme to write out the individual segments in fasta format (i.e. with an informative fasta header) into a single fasta file.
# Modify your Python script/programme to include the partial sliding window segments that we get at the end of the sequence.

# Note that all of the above 'modifications' could/should be part of a single Python script/programme! For example, you might find it easier to add processing step (a), ensure it is working properly, then try adding (b), and so on.


import subprocess

exon = subprocess.run("grep -v '>' remote_exon01.fasta", shell=True, capture_output=True, text=True).stdout.strip()
print(exon)
print(len(exon))

with open('remote_exon01.fasta') as exon_file:
    exon = exon_file.read().split()[1]
    print(exon)
    print(len(exon))
    
window_start= 0
window_end = 30

while window_end < len(exon):
    current_window = exon[window_start:window_end]
    current_window = str(current_window)
    gc_content = (current_window.upper().count("G") + current_window.upper().count("G")) / len(current_window) * 100
    print(current_window, str(round(gc_content)) + '%')
    window_start = window_start +3
    window_end = window_end +3

gc_content_exon = (exon.upper().count("G") + exon.upper().count("C")) / len(exon) * 100
print(f"GC content of the sequence is {round(gc_content_exon)}%")
# while window < len(exon):
#     print(exon[window])
#     window = window + 3


# input: sequence DONE

# 30 base long segments, move on by 3

# output: each sliding window segment

# print the percentage GC content of each sliding window segment and the sequence.

# write out the individual segments in fasta format (i.e. with an informative fasta header) into individual fasta files.

# write out the individual segments in fasta format (i.e. with an informative fasta header) into a single fasta file.

# include the partial sliding window segments that we get at the end of the sequence.

# ------------------------ SECOND SOLUTION
# window_start = 0
# window_end = 0

# window_size = 30
# offset = 3

# def gc_content(dna):
#     dna = dna.upper()
#     if len(dna) == 0:
#         return(0)
#     total_gc = dna.count("C") + dna.count("G")
#     percentage_gc = round(total_gc/len(dna)*100)
#     return(percentage_gc)

# window_end = window_size


# with open('remote_exon01.fasta') as exon_file, open('sliding_exon.fasta', 'w') as sliding_exon:
#     # create a new variable and since the file has two lines the second line is our exon
#     exon = exon_file.readlines()[1]
#     print(exon)

#     exon = exon.upper()
#     # apply sliding window logic
#     # COUNT FOR THE FASTA FILE
#     count = 0
#     for i in range(len(exon)):
#         count += 1
#         window = exon[window_start:window_end]

#         percent_gc = gc_content(window)
#         print(window + " " + str(percent_gc)+ "%  " + str(window_start))

#         fasta_header = f">AJ223353_sliding_window{count}_gc_content{percent_gc}_length{len(window)}"
#         sliding_exon.write(fasta_header + "\n" + window + "\n\n")
#         window_start += offset
#         window_end += offset

#         if window_start == len(exon):
#             break
    



        