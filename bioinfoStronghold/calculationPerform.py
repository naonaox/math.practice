from bioinfo_class import *

'''dna problem'''
inpath='./input/rosalind_dna.txt'
outpath='./output/rosalind_dna.txt'

analysisIn=stringCalculation(inpath)
dnaout=analysisIn.dna_prob()
with open(outpath,'w') as fout:
    fout.write(dnaout)