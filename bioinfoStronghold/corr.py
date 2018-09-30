#Error Correction in Reads

import sys
from Bio import SeqIO
from collections import defaultdict

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))

def reverseComplement(oseq):
    rdic={'A':'T','T':'A','C':'G','G':'C'}
    nseq=''.join([rdic[oseq[x]] for x in range(len(oseq)-1,-1,-1)])
    return nseq

def hamdistance(s1,s2):
    dis1=len([i for i in range(len(s1)) if s1[i]!=s2[i]])
    dis2=len([i for i in range(len(s1)) if s1[i]!=reverseComplement(s2)[i]])
    return (dis1,s2) if dis1<dis2 else (dis2,reverseComplement(s2))

def correctionSeq(sequences):
    seqcount={}
    for s in sequences:
        if s not in seqcount and reverseComplement(s) not in seqcount:
            seqcount[s]=1
        elif s in seqcount:
            seqcount[s]+=1
        elif reverseComplement(s) in seqcount:
            seqcount[reverseComplement(s)]+=1
    wrongseq=[x for x in seqcount if seqcount[x]==1]
    corrects=[x for x in seqcount if seqcount[x]>1]
    corrections={}
    for item in wrongseq:
        for corr in corrects:
            ham,cseq=hamdistance(item,corr)
            if ham==1:
                corrections[item]=cseq
                break
    return corrections

if __name__=='__main__':
    infile,outfile=sys.argv[1],sys.argv[2]
    seqs=[str(x) for x in list(readfasta(infile).values())]
    cout=correctionSeq(seqs)
    with open(outfile,'w') as whandle:
        whandle.write('\n'.join([x+'->'+cout[x] for x in cout]))
        whandle.write('\n')