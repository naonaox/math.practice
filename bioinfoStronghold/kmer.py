#K-mer Composition

import sys
from Bio import SeqIO
from itertools import product
from collections import defaultdict

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))

def kmer(k):
    klist=[list(x) for x in list(product('ACGT',repeat=k))]
    return [''.join(x) for x in klist]

def kmer_composition(seq,k):
    kmers=kmer(k)
    kcount=dict(zip(kmers,[0]*len(kmers)))
    for i in range(0,len(seq)-k+1):
        kcount[seq[i:i+k]]+=1
    return [kcount[x] for x in kmers]

if __name__=='__main__':
    infile,outfile=sys.argv[1],sys.argv[2]
    sequence=str(list(readfasta(infile).values())[0])
    comp=kmer_composition(sequence,4)
    with open(outfile,'w') as whandle:
        whandle.write(' '.join([str(x) for x in comp]))
        whandle.write('\n')