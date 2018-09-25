#Mortal Fibonacci Rabbit

import sys
import numpy as np

def numberstringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    str0=strs[0]
    nums=[int(x) for x in str0.split(' ')]
    return nums

def mortal_fibrats(month,longev,pair=1):
    mature_rab = [0]*month#np.zeros(month,int)
    baby_rab = [0]*month#np.zeros(month,int)
    mature_rab[0],baby_rab[0]=0,1
    for i in range(1, month):
        mature_rab[i]=mature_rab[i - 1] + baby_rab[i - 1]-baby_rab[i-longev]
        baby_rab[i] = mature_rab[i - 1] * pair
    return mature_rab[-1]+baby_rab[-1]

infile=sys.argv[1]
outfile=sys.argv[2]

readfile=numberstringRead(infile)
n,m=readfile[0],readfile[1]
fib_rats=mortal_fibrats(n,m)
with open(outfile,'w') as handle:
    handle.write(str(int(fib_rats))+'\n')