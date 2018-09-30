#Longest increasing subsequnce

import sys
import numpy as np
from collections import defaultdict

def longestSubsequence(numlist):
    increasing,decreasing=defaultdict(list),defaultdict(list)
    for i in range(len(numlist)):
        inckeys,deckeys=list(sorted(list(increasing.keys()))),list(sorted(list(decreasing.keys())))
        for j in inckeys:
            preinc=sorted(increasing[j],key=lambda x:x[-1])
            for item in preinc:
                if item[-1]<numlist[i]:
                    newitem=item.copy()
                    newitem.append(numlist[i])
                    increasing[j+1].append(newitem)
                    increasing[j+1]=[sorted(increasing[j+1],key=lambda x:x[-1])[0]]
                    break
        for k in deckeys:
            predec=list(reversed(list(sorted(decreasing[k],key=lambda x:x[-1]))))
            for item in predec:
                if item[-1]>numlist[i]:
                    newitem=item.copy()
                    newitem.append(numlist[i])
                    decreasing[k+1].append(newitem)
                    decreasing[k+1]=[sorted(decreasing[k+1],key=lambda x:x[-1])[-1]]
                    break
        increasing[1].append([numlist[i]])
        increasing[1]=[[np.min([x[0] for x in increasing[1]])]]
        decreasing[1].append([numlist[i]])
        decreasing[1]=[[np.max([x[0] for x in decreasing[1]])]]
    return increasing[list(sorted(list(increasing.keys())))[-1]][0],decreasing[list(sorted(list(decreasing.keys())))[-1]][0]

if __name__=='__main__':
    infile=sys.argv[1]
    outfile=sys.argv[2]

    with open(infile) as rhandle:
        rreads=rhandle.read().split('\n')
        numarray=[int(x) for x in rreads[1].split(' ')]
    linc,ldec=longestSubsequence(numarray)
    with open(outfile,'w') as whandle:
        whandle.write(' '.join([str(x) for x in linc])+'\n')
        whandle.write(' '.join([str(x) for x in ldec])+'\n')