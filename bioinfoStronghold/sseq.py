#Finding a Spliced Motif

import sys
from Bio import SeqIO

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return names,seqs

def indices(longseq,subseq):
    idc=[-1]
    for i in range(len(subseq)):
        for j in range(idc[-1]+1,len(longseq)):
            if longseq[j]==subseq[i]:
                idc.append(j)
                break
    return [x+1 for x in idc[1:]]

if __name__=='__main__':
    infile,outfile=sys.argv[1],sys.argv[2]
    faread=readfasta(infile)
    lseq,sseq=str(faread[1][0]),str(faread[1][1])
    idc=indices(lseq,sseq)
    with open(outfile,'w') as whandle:
        whandle.write(' '.join([str(x) for x in idc])+'\n')