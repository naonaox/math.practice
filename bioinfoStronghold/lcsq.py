#Finding a Shared Spliced Motif

from Bio import SeqIO
import numpy as np
import sys

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))


def common_sub_tbl(seq1,seq2):
    commontbl=np.zeros((len(seq1)+1,len(seq2)+1),dtype=int)
    for i in range(1,len(seq1)+1):
        for j in range(1,len(seq2)+1):
            if seq1[i-1]==seq2[j-1]:
                commontbl[i,j]=commontbl[i-1,j-1]+1
            else:
                commontbl[i,j]=max(commontbl[i-1,j],commontbl[i,j-1])
    return commontbl

def read_out_lcs(comtbl,seq1,seq2,i,j):
    #start with i=seq1len+1,j=seq2len+1
    if i==0 or j==0:
        return ['']
    if seq1[i-1]==seq2[j-1]:
        return [x+seq1[i-1] for x in read_out_lcs(comtbl,seq1,seq2,i-1,j-1)]
    R=set()
    if comtbl[i,j-1]>=comtbl[i-1,j]:# and i>=1 and j>=1:
        for x in read_out_lcs(comtbl,seq1,seq2,i,j-1):
            R.add(x)
    if comtbl[i-1,j]>=comtbl[i,j-1]:#== and i>=1 and j>=1:
        for x in read_out_lcs(comtbl,seq1,seq2,i-1,j):
            R.add(x)
    return R

def lcs(combtbl,seq1,seq2):
    i,j=len(seq1),len(seq2)
    cseq=''
    while i>0 and j>0:
        if combtbl[i,j]==combtbl[i-1,j]:
            i-=1
        elif combtbl[i,j]==combtbl[i,j-1]:
            j-=1
        else:
            cseq=seq1[i-1]+cseq
            i-=1
            j-=1
        '''
        if seq1[i-1]==seq2[j-1]:
            cseq=seq1[i-1]+cseq
            i-=1
            j-=1
        else:
            if combtbl[i,j-1]>=combtbl[i-1,j]:
                j-=1
            elif combtbl[i-1,j]>=combtbl[i,j-1]:
                i-=1
        '''
    return cseq

if __name__=='__main__':
    infile,outfile=sys.argv[1],sys.argv[2]
    sequences=[str(x) for x in readfasta(infile).values()]
    dna1,dna2=sequences[0],sequences[1]
    common_tbl=common_sub_tbl(dna1,dna2)
    common_str=lcs(common_tbl,dna1,dna2)
    with open(outfile,'w') as whandle:
        whandle.write(common_str+'\n')