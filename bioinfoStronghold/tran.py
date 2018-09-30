#Transitions and Transversions

import sys
from Bio import SeqIO

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return names,seqs

def R(s1,s2):
    examtransition=[['A','G'],['G','A'],['C','T'],['T','C']]
    transition,transversion=0.0,0.0
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            continue
        if [s1[i],s2[i]] in examtransition:
            transition+=1
        else:
            transversion+=1
    return transition/transversion

if __name__=='__main__':
    infile,outfile=sys.argv[1],sys.argv[2]
    reads=readfasta(infile)[1]
    seq1,seq2=str(reads[0]),str(reads[1])
    tranRate=R(seq1,seq2)
    with open(outfile,'w') as whandle:
        whandle.write(str(tranRate)+'\n')