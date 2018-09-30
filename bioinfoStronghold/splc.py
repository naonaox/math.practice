#RNA Splicing

import sys
from Bio import SeqIO

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return names,seqs

codon_table={"UUU":"F","CUU":"L","AUU":"I","GUU":"V","UUC":"F","CUC":"L","AUC":"I","GUC":"V","UUA":"L","CUA":"L","AUA":"I","GUA":"V","UUG":"L","CUG":"L","AUG":"M","GUG":"V","UCU":"S","CCU":"P","ACU":"T","GCU":"A","UCC":"S","CCC":"P","ACC":"T","GCC":"A","UCA":"S","CCA":"P","ACA":"T","GCA":"A","UCG":"S","CCG":"P","ACG":"T","GCG":"A","UAU":"Y","CAU":"H","AAU":"N","GAU":"D","UAC":"Y","CAC":"H","AAC":"N","GAC":"D","UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E","UGU":"C","CGU":"R","AGU":"S","GGU":"G","UGC":"C","CGC":"R","AGC":"S","GGC":"G","UGA":"Stop","CGA":"R","AGA":"R","GGA":"G","UGG":"W","CGG":"R","AGG":"R","GGG":"G"}

def reverseComplement(oseq):
    rdic={'A':'T','T':'A','C':'G','G':'C'}
    rseq=''
    for b in oseq.upper():
        rseq=rdic[b]+rseq
    return rseq

def spliceNtranslate(oseq,introns):
    sseq=oseq
    for i in introns:
        sseq=sseq.replace(i,'')
    rcseq=sseq.replace('T','U')
    proteinseq=''
    startsite=0
    for i in range(len(rcseq)):
        if startsite!=0:
            startsite+=1
        if startsite%3==1:
            proteinseq+=codon_table[rcseq[i:i+3]]
        if codon_table[rcseq[i:i+3]]=='M' and proteinseq=='':
            proteinseq+='M'
            startsite=1
        if 'Stop' in proteinseq:
            break
    return proteinseq.replace('Stop','')

if __name__=='__main__':
    infile=sys.argv[1]
    outfile=sys.argv[2]

    names,reads=readfasta(infile)
    reads=[str(x) for x in reads]
    protein=spliceNtranslate(reads[0],reads[1:])
    with open(outfile,'w') as handle:
        handle.write(protein+'\n')