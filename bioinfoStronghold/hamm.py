#Counting Point Mutations

import sys

def stringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    return strs

def hamming_distance(str1,str2):
    '''str1 str2 have same length'''
    STR1=list(str1.upper())
    STR2=list(str2.upper())
    equals=[STR1[x]==STR2[x] for x in range(len(STR1))]
    return equals.count(False)

infile=sys.argv[1]
outfile=sys.argv[2]

dna_strs=stringRead(infile)
ham_distance=hamming_distance(dna_strs[0],dna_strs[1])
with open(outfile,'w') as outf:
    outf.write(str(ham_distance)+'\n')