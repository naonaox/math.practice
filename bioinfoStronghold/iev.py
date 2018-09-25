#Calculating Expected Offspring
'''
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
'''

import sys
import numpy as np

def numberstringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    str0=strs[0]
    nums=[int(x) for x in str0.split(' ')]
    return nums

offsprings=[(1,0,0),(0.5,0.5,0),(0,1,0),(0.25,0.5,0.25),(0,0.5,0.5),(0,0,1)]

def off_phenotype(pairarray,numoff):
    x1=np.sum([a*b[0] for a,b in zip(pairarray,offsprings)])
    x2=np.sum([a*b[1] for a,b in zip(pairarray,offsprings)])
    x3=np.sum([a*b[2] for a,b in zip(pairarray,offsprings)])
    return x1*numoff,x2*numoff,x3*numoff

if __name__=='__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]

    nums=[float(x) for x in numberstringRead(infile)]
    dom_homo,dom_hete,rec_homo=off_phenotype(nums,2)
    with open(outfile,'w') as handle:
        handle.write(str(dom_homo+dom_hete)+'\n')
