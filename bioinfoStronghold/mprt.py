#Finding a Protein Motif

import sys,urllib
from Bio import SeqIO

def readfasta_online(inpath):
    with urllib.request.urlopen(inpath) as handle:
        seq=''.join(str(handle.read()).split('\\n')[1:])
    return seq

def stringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    return strs

#N-glycosylation motif is written as N{P}[ST]{P}
def N_glycosylation_position(protein_seq):
    Npos=[]
    for i in range(len(protein_seq)-2):
        if protein_seq[i]=='N':
            if protein_seq[i+1]!='P' and protein_seq[i+3]!='P' and protein_seq[i+2] in 'ST':
                Npos.append(i+1)
    return Npos

if __name__=='__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    sequencename=[x for x in stringRead(infile) if x!='']
    sequence_N_pos={}
    for sname in sequencename:
        fastapath='http://www.uniprot.org/uniprot/'+sname+".fasta"
        seqread=readfasta_online(fastapath)
        sequence_N_pos[sname]=N_glycosylation_position(seqread)
    with open(outfile,'w') as handle:
        for item in sequencename:
            if sequence_N_pos[item]!=[]:
                handle.write(item+'\n'+' '.join([str(x) for x in sequence_N_pos[item]])+'\n')