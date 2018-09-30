#Finding a Shared Spliced Motif

from Bio import SeqIO
from itertools import combinations

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))

print(list(combinations('AGCGTA',3)))