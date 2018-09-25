#Consensus and Profile

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

def base_array(sequences):
    '''create nd array for dna'''
    seqsplit_bases=[list(x) for x in sequences]
    dna_array=np.array(seqsplit_bases)
    return dna_array

def basecount_array(seqbase_array):
    '''create nd array for A,C,G,T count'''
    countarray=np.zeros((4,len(seqbase_array[0,:])))
    for i in range(len(seqbase_array[0,:])):
        countarray[0,i]=np.count_nonzero(seqbase_array[:,i]=='A')
        countarray[1,i]=np.count_nonzero(seqbase_array[:,i]=='C')
        countarray[2,i]=np.count_nonzero(seqbase_array[:,i]=='G')
        countarray[3,i]=np.count_nonzero(seqbase_array[:,i]=='T')
    return countarray

def args_from_count(countbase_array):
    '''return consensus args'''
    maxargs=np.zeros(len(countbase_array[0,:]))
    for i in range(len(countbase_array[0,:])):
        maxargs[i]=np.argmax(countbase_array[:,i])
    return maxargs

dicbase={0:'A',1:'C',2:'G',3:'T'}

def consensus(sequences_input):
    dna_base_array=base_array(sequences_input)
    base_count=basecount_array(dna_base_array)
    args_max_array=args_from_count(base_count)
    argslist=[int(x) for x in args_max_array]
    outseqlist=[dicbase[x] for x in argslist]
    return ''.join(outseqlist),base_count

infile=sys.argv[1]
outfile=sys.argv[2]

seqdic=readfasta(infile)
dna_sequences=seqdic.values()
outsequence,count_array=consensus(dna_sequences)
outmatrix=[]
for i in range(len(count_array[:,0])):
    outmatrix.append(' '.join([str(int(x)) for x in count_array[i,:]]))
with open(outfile,'w') as handle:
    handle.write(outsequence+'\n')
    for i in range(len(dicbase)):
        handle.write(dicbase[i]+': '+outmatrix[i]+'\n')