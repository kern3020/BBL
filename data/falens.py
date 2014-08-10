#!/usr/bin/python
import sys
from Bio import SeqIO
myCount = 0
myAccept = 0
filename = sys.argv[1]
cutoff = 1.0e-08
print("reading:{0}  cutoff:{1}".format(filename, cutoff))
# ugh need to add sequence lenghts 
handle = open(filename, "r")
for record in SeqIO.parse(handle, "fasta") :
    output  ='\t'.join([record.id,str(len(record.seq)) ]) 
    print(output)
handle.close()
