#Independent Alleles

import sys,math
from iprb import C

def numberstringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    str0=strs[0]
    nums=[int(x) for x in str0.split(' ')]
    return nums

def mendels_second_heteroProb(k,N):
    #k=generation
    #N=least AaBb number
    probability=0
    for i in range(N,2**k+1):
        prob=C(2**k,i)*0.25**i*0.75**(2**k-i)
        probability+=prob
    return probability

if __name__=='__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]

    readfile = numberstringRead(infile)
    k_generation,N_least=readfile[0],readfile[1]
    outprob=mendels_second_heteroProb(k_generation,N_least)
    with open(outfile,'w') as handle:
        handle.write(str(round(outprob,6))+'\n')