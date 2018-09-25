#Finding a Motif in DNA

import sys

def stringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    return strs

def substring_positions(orgnl_str,sub_str):
    subpos=[]
    for i in range(0,len(orgnl_str)-len(sub_str)):
        if orgnl_str[i:i+len(sub_str)]==sub_str:
            subpos.append(i+1)
    return subpos

infile=sys.argv[1]
outfile=sys.argv[2]

strs=stringRead(infile)
substr_pos=substring_positions(strs[0],strs[1])
outputinfo=' '.join([str(x) for x in substr_pos])
with open(outfile,'w') as outf:
    outf.write(outputinfo+'\n')