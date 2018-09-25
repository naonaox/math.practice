#Finding a Shared Motif
#longest common substring

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

def longest_common_substring(strcollection):
    shortest=sorted([(x,len(x)) for x in strcollection],key=lambda x:x[1])[0][0]
    motif,mlen,notshare=[shortest],len(shortest),True
    common_substr=''
    while notshare:
        for item in motif:
            notshare=False
            for sequence in strcollection:
                if item not in sequence:
                    notshare=True
            if notshare==False:
                common_substr=item
                break
        mlen-=1
        motif=set([shortest[i:i+mlen] for i in range(len(shortest)-mlen+1)])
    return common_substr

if __name__=='__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    fastainfo = readfasta(infile)
    sequences=fastainfo.values()
    lcsm=longest_common_substring(set(sequences))
    with open(outfile,'w') as handle:
        handle.write(str(lcsm)+'\n')