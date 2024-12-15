#!/usr/bin/python3

# Module loading
import os

# Define the function with defaults where possible
def new_find_my_kmers(dna,ksize=2,minkfreq=2) :
   kmersfound = []
   kmerstarts = list(range(0,len(dna)))
   for base in kmerstarts:
       if (base+ksize) < len(dna)+1:
           seqout = (dna)[base:base+ksize]
           kmersfound = kmersfound + [seqout] 
   nrset = list(set(kmersfound))
   returnstuff = []
   for kfreqfind in nrset:
       if kmersfound.count(kfreqfind) > minkfreq :
           returnstuff.append(kfreqfind.upper()+": "+str(kmersfound.count(kfreqfind)))
   return returnstuff


# Define the inputs with defaults if user doesnt supply values
inputdna = input ("What is your sequence?\n\t").upper()

if inputdna :

  inputksize = int ( input ("What kmer size shall I use?\n\t") or 2)
  if (inputksize < 2 or inputksize >= len(inputdna) or inputksize > 50) :
     inputksize = 2
     print("Inappropriate value chosen, resetting to 2\n\t")
  inputminkfreq = int ( input ("What minimum frequency shall I use?\n\t") or 2)
  print("Thanks!  Processing:\n"+inputdna+"\n for a kmersize of "
   +str(inputksize)+",\n reporting frequencies greater than "
   +str(inputminkfreq)+"\n")
  # Process the input by calling the find_my_kmers function
  outputstuff = new_find_my_kmers(dna=inputdna,ksize=inputksize,minkfreq=inputminkfreq)
  outputstuff.sort()
  # Open the pipe to an output file for our results
  myfilename="kmerouts"+"_KMER"+str(inputksize)+"_MIN"+str(inputminkfreq)+".txt"
  outputfilepipe = open(myfilename,"w")
  # See if there is anything to output first
  if len(outputstuff) == 0 :
    print("No kmers met the criteria, so no outputs to file!\n")
    outputfilepipe.close()
  else:
    print("Results:\n")
    print(outputstuff)
    # Send the outputs to the file via the pipe,
    # summary info first, then kmer frequencies
    outputfilepipe.write("### Kmer analysis\n#SQ "+str(inputdna)+
     "\n#KMER "+str(inputksize)+
     "\n#MIN "+str(inputminkfreq)+"\n")
    for freqseq in outputstuff :
        outputfilepipe.write(freqseq+"\n")
    outputfilepipe.write("\n")
    # Dont forget to close the output connection!
    outputfilepipe.close()
    # Show the saved file outputs using a system call
    print("\n\nContents of the output:\n")
    syscmd="cat " + myfilename
    os.system(syscmd)

else :
  print ("Sorry, really can\'t do any of this without a sequence!\n")