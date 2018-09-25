from collections import defaultdict
import sys

def stringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    return strs

def baseCount_dna(dnaseq):
    basedic=defaultdict(int)
    DNA=dnaseq.upper()
    for b in DNA:
        if b in 'ACTG':
            basedic[b]+=1
    return basedic

infile=sys.argv[1]
outfile=sys.argv[2]

stringextracted=stringRead(infile)
dnabase=baseCount_dna(stringextracted[0])
outputstr=' '.join([str(dnabase['A']),str(dnabase['C']),str(dnabase['G']),str(dnabase['T'])])

with open(outfile,'w') as fout:
    fout.write(outputstr+'\n')