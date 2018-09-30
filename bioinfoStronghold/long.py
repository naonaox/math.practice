#Genome Assembly as Shortest Superstring

import sys
from Bio import SeqIO
import itertools

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))

def overlap_reads(pair):
    minlen=len(pair[0]) if len(pair[0])<len(pair[1]) else len(pair[1])
    for i in range(minlen,int(minlen/2),-1):
        if pair[0][-i:]==pair[1][:i]:
            return (pair[0],pair[1]),i
        elif pair[1][-i:]==pair[0][:i]:
            return (pair[1],pair[0]),i
    return False,0

def assembly(seqdic):
    pairs=itertools.combinations([str(x) for x in seqdic.values()],2)
    overlens,overpairs=[],[]
    for p in pairs:
        overcheck=overlap_reads(p)
        if overcheck[0]:
            overlens.append(overcheck[1])
            overpairs.append(overcheck[0])
    heads=[x[0] for x in overpairs]
    tails=[x[1] for x in overpairs]
    head=[x for x in heads if x not in tails][0]
    tail=[x for x in tails if x not in heads][0]
    overdic={}
    lendic=dict(zip(overpairs,overlens))
    for p in overpairs:
        overdic[p[0]]=p[1]
    assembly=head+overdic[head][lendic[(head,overdic[head])]:]
    newhead=overdic[head]
    while newhead!=tail:
        assembly+=overdic[newhead][lendic[(newhead,overdic[newhead])]:]
        newhead=overdic[newhead]
    return assembly

if __name__=='__main__':
    infile=sys.argv[1]
    outfile=sys.argv[2]

    fastareads=readfasta(infile)
    assembout=assembly(fastareads)
    with open(outfile,'w') as whandle:
        whandle.write(assembout+'\n')