#Perfect Matchings and RNA Secondary Structures

from itertools import permutations
from Bio import SeqIO
from collections import defaultdict
import sys,math

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))

def RNAMatching(rnaseq):
    base=defaultdict(list)
    for i in range(len(rnaseq)):
        base[rnaseq[i]].append(rnaseq[i]+str(i))
    '''
    AUmatch=[list(zip(x,base['U'])) for x in permutations(base['A'],len(base['A']))]
    CGmatch=[list(zip(x,base['G'])) for x in permutations(base['C'],len(base['G']))]
    unqualified_distance=[1,-1,-len(rnaseq)+1,len(rnaseq)-1]
    AUperfectmatch,CGperfectmatch=[],[]
    
    for i in range(len(AUmatch)):
        qualified=True
        for j in range(len(AUmatch[i])):
            if int(AUmatch[i][j][0][1])-int(AUmatch[i][j][1][1]) in unqualified_distance:
                qualified=False
                break
        if qualified:
            AUperfectmatch.append(AUmatch[i])
    for i in range(len(CGmatch)):
        qualified=True
        for j in range(len(CGmatch[i])):
            if int(CGmatch[i][j][0][1])-int(CGmatch[i][j][1][1]) in unqualified_distance:
                qualified=False
                break
        if qualified:
            CGperfectmatch.append(CGmatch[i])
    '''
    #return len(AUmatch)*len(CGmatch)
    return math.factorial(len(base['A']))*math.factorial(len(base['C']))

'''
A=['A1','A2','A3']
U=['U4','U5','U6']

test=[list(zip(x,U)) for x in permutations(A,3)]
print(test)
'''

if __name__=='__main__':
    infile=sys.argv[1]
    outfile=sys.argv[2]

    seq=list(readfasta(infile).values())[0]
    perfectmatchings=RNAMatching(seq)

    with open(outfile,'w') as whandle:
        whandle.write(str(perfectmatchings)+'\n')