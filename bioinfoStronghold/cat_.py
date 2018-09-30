#Catalan Numbers and RNA Secondary Structures

import sys
import numpy as np
from Bio import SeqIO

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))

def catalan(seq):
    if seq not in cache:
        tmp=[]
        for k in range(1,len(seq),2):
            tmp.append(catalan(seq[1:k])*cache[seq[0]+seq[k]]*catalan(seq[k+1:]))
        cache[seq]=sum(tmp)
    return cache[seq]

if __name__=='__main__':
    infile=sys.argv[1]
    fasta=readfasta(infile)
    seq=str(list(fasta.values())[0])
    cache = {'': 1, 'A': 0, 'C': 0, 'G': 0, 'U': 0, 'AA': 0, 'AC': 0, 'AG': 0, 'AU': 1, 'CA': 0, 'CC': 0,
             'CG': 1, 'CU': 0, 'GA': 0, 'GC': 1, 'GG': 0, 'GU': 0, 'UA': 1, 'UC': 0, 'UG': 0, 'UU': 0}
    print(catalan(seq)%1000000)