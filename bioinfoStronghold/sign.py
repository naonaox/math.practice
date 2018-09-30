#Enumerating Oriented Gene Orderings

import sys
from itertools import permutations,product

def numberstringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    str0=strs[0]
    nums=[int(x) for x in str0.split(' ')]
    return nums

def signed_perm(k):
    l1=range(1,k+1)
    originalperms=list(permutations(l1,k))
    minusassaign=list(product([-1,1],repeat=k))
    perms=[[x[i]*y[i] for i in range(len(x))] for x in originalperms for y in minusassaign]
    return perms

if __name__=='__main__':
    infile,outfile=sys.argv[1],sys.argv[2]
    n=numberstringRead(infile)[0]
    sp=signed_perm(n)
    with open(outfile,'w') as whandle:
        whandle.write(str(len(sp))+'\n')
        for item in sp:
            for i in range(len(item)):
                if i!=len(item)-1:
                    whandle.write(str(item[i])+' ')
                else:
                    whandle.write(str(item[i])+'\n')