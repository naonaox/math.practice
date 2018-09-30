#Translating RNA into Protein

import sys

def stringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    return strs

codon_table={"UUU":"F","CUU":"L","AUU":"I","GUU":"V","UUC":"F","CUC":"L","AUC":"I","GUC":"V","UUA":"L","CUA":"L","AUA":"I","GUA":"V","UUG":"L","CUG":"L","AUG":"M","GUG":"V","UCU":"S","CCU":"P","ACU":"T","GCU":"A","UCC":"S","CCC":"P","ACC":"T","GCC":"A","UCA":"S","CCA":"P","ACA":"T","GCA":"A","UCG":"S","CCG":"P","ACG":"T","GCG":"A","UAU":"Y","CAU":"H","AAU":"N","GAU":"D","UAC":"Y","CAC":"H","AAC":"N","GAC":"D","UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E","UGU":"C","CGU":"R","AGU":"S","GGU":"G","UGC":"C","CGC":"R","AGC":"S","GGC":"G","UGA":"Stop","CGA":"R","AGA":"R","GGA":"G","UGG":"W","CGG":"R","AGG":"R","GGG":"G"}

def translate_RNA(rnaseq):
    codons=[rnaseq[x:x+3] for x in range(0,len(rnaseq)-3,3)]
    proteins=[codon_table[x] for x in codons]
    return ''.join(proteins)

infile=sys.argv[1]
outfile=sys.argv[2]

rnaseqs=stringRead(infile)
protein_seq=translate_RNA(rnaseqs[0])
with open(outfile,'w') as outf:
    outf.write(protein_seq+'\n')