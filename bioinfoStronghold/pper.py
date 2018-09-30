#Partial Permutations

import math,sys

def numberstringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    str0=strs[0]
    nums=[int(x) for x in str0.split(' ')]
    return nums

def A(n,r):
    return math.factorial(n)/math.factorial(n-r)

if __name__=='__main__':
    infile=sys.argv[1]
    outfile=sys.argv[2]

    nums=numberstringRead(infile)
    outnums=A(nums[0],nums[1])%1000000
    with open(outfile,'w') as whandle:
        whandle.write(str(int(outnums))+'\n')