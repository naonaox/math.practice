from bioinfo_function import *

class stringCalculation():
    def __init__(self,filepath,filetype='normal'):
        self.strs=[]
        with open(filepath) as infile:
            self.strs=infile.read().split('\n')
    def dna_prob(self):
        outbase=baseCount_dna(self.strs[0])
        return str(outbase['A'])+' '+str(outbase['C'])+' '+str(outbase['G'])+' '+str(outbase['T'])+'\n'