#Inferring mRAN from Protein

import sys
from collections import defaultdict

def stringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    return strs

codon_table={"UUU":"F","CUU":"L","AUU":"I","GUU":"V","UUC":"F","CUC":"L","AUC":"I","GUC":"V","UUA":"L","CUA":"L","AUA":"I","GUA":"V","UUG":"L","CUG":"L","AUG":"M","GUG":"V","UCU":"S","CCU":"P","ACU":"T","GCU":"A","UCC":"S","CCC":"P","ACC":"T","GCC":"A","UCA":"S","CCA":"P","ACA":"T","GCA":"A","UCG":"S","CCG":"P","ACG":"T","GCG":"A","UAU":"Y","CAU":"H","AAU":"N","GAU":"D","UAC":"Y","CAC":"H","AAC":"N","GAC":"D","UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E","UGU":"C","CGU":"R","AGU":"S","GGU":"G","UGC":"C","CGC":"R","AGC":"S","GGC":"G","UGA":"Stop","CGA":"R","AGA":"R","GGA":"G","UGG":"W","CGG":"R","AGG":"R","GGG":"G"}

reverse_table=defaultdict(list)
for ckey in codon_table:
    reverse_table[codon_table[ckey]].append(ckey)

if __name__=='__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    protein=stringRead(infile)[0]
    combination=1
    for aa in protein:
        combination*=len(reverse_table[aa])
    combination*=len(reverse_table['Stop'])
    with open(outfile,'w') as handle:
        handle.write(str(combination%1000000)+'\n')