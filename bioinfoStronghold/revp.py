#Locating Restriction Sites
'''
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
'''

import sys
from Bio import SeqIO

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))

def reverseComplement(oseq):
    rdic={'A':'T','T':'A','C':'G','G':'C'}
    rseq=''
    for b in oseq.upper():
        rseq=rdic[b]+rseq
    return rseq

def isRevPalindrom(palseq):
    if palseq==reverseComplement(palseq):
        return True
    return False

def findRevPalindrom(dnaseq,kmin,kmax):
    palPos=[]
    for i in range(len(dnaseq)-kmin+1):
        for j in range(kmin,kmax+1):
            if i+j<=len(dnaseq):
                if isRevPalindrom(dnaseq[i:i+j]):
                    palPos.append((i+1,j))
    return palPos

if __name__=='__main__':
    infile=sys.argv[1]
    outfile=sys.argv[2]

    dnaseq=str(list(readfasta(infile).values())[0])
    palpos=findRevPalindrom(dnaseq,4,12)
    with open(outfile,'w') as handle:
        for item in palpos:
            handle.write(str(item[0])+' '+str(item[1])+'\n')