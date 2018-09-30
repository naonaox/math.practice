#Enumerating Gene Orders

import sys
from itertools import permutations

def numberstringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    str0=strs[0]
    nums=[int(x) for x in str0.split(' ')]
    return nums

if __name__=='__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    numlist=numberstringRead(infile)
    outlist=list(permutations(range(1,numlist[0]+1),numlist[0]))
    with open(outfile,'w') as handle:
        handle.write(str(len(outlist))+'\n')
        for perm in outlist:
            for i in range(len(perm)):
                if i!=len(perm)-1:
                    handle.write(str(perm[i])+' ')
                else:
                    handle.write(str(perm[i])+'\n')
