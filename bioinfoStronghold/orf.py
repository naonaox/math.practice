#Open Reading Frames

import sys
from Bio import SeqIO

codon_table={"UUU":"F","CUU":"L","AUU":"I","GUU":"V","UUC":"F","CUC":"L","AUC":"I","GUC":"V","UUA":"L","CUA":"L","AUA":"I","GUA":"V","UUG":"L","CUG":"L","AUG":"M","GUG":"V","UCU":"S","CCU":"P","ACU":"T","GCU":"A","UCC":"S","CCC":"P","ACC":"T","GCC":"A","UCA":"S","CCA":"P","ACA":"T","GCA":"A","UCG":"S","CCG":"P","ACG":"T","GCG":"A","UAU":"Y","CAU":"H","AAU":"N","GAU":"D","UAC":"Y","CAC":"H","AAC":"N","GAC":"D","UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E","UGU":"C","CGU":"R","AGU":"S","GGU":"G","UGC":"C","CGC":"R","AGC":"S","GGC":"G","UGA":"Stop","CGA":"R","AGA":"R","GGA":"G","UGG":"W","CGG":"R","AGG":"R","GGG":"G"}
def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))

def reverse_complement(dseq):
    com={'A':'T','T':'A','C':'G','G':'C'}
    nseq=''
    for b in dseq.upper():
        nseq=com[b]+nseq
    return nseq

def translating(dnaseq):
    rnaseq=reverse_complement(dnaseq.upper()).replace('T','U')
    aaseq=[]
    for i in range(len(rnaseq)-2):
        aa=codon_table[rnaseq[i:i+3]]
        for j in range(len(aaseq)):
            if 'Stop' not in aaseq[j]:
                aaseq[j]+=aa
        if aa=='M':
            aaseq.append(aa)
    return [x.replace('Stop','') for x in aaseq]

if __name__=='__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]

    dnaread=str(list(readfasta(infile).values())[0])
    proteinseq=translating(dnaread)
    with open(outfile,'w') as handle:
        for item in proteinseq:
            handle.write(item+'\n')