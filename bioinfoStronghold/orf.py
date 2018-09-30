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
    rnaseq=dnaseq.replace('T','U')#
    rnaseq2=reverse_complement(dnaseq.upper()).replace('T','U')
    aaseq,aaseq2=[],[]
    aapos,aapos2=[],[]
    for i in range(len(rnaseq)-2):
        aapos=[x+1 for x in aapos]
        aa=codon_table[rnaseq[i:i+3]]
        for j in range(len(aaseq)):
            if 'Stop' not in aaseq[j] and aapos[j]%3==1:
                aaseq[j]+=aa
        if aa=='M':
            aaseq.append(aa)
            aapos.append(1)

        aapos2 = [x + 1 for x in aapos2]
        aa2 = codon_table[rnaseq2[i:i + 3]]
        for j in range(len(aaseq2)):
            if 'Stop' not in aaseq2[j] and aapos2[j] % 3 == 1:
                aaseq2[j] += aa2
        if aa2 == 'M':
            aaseq2.append(aa2)
            aapos2.append(1)
    aaout=set(aaseq+aaseq2)
    return [x.replace('Stop','') for x in aaout if 'Stop' in x]

if __name__=='__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]

    dnaread=str(list(readfasta(infile).values())[0])
    proteinseq=translating(dnaread)
    with open(outfile,'w') as handle:
        for item in proteinseq:
            handle.write(item+'\n')