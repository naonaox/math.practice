#Speeding Up Motif Finding

import sys,datetime
from Bio import SeqIO

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))

def failure_array(seq):
    f=[0]*(len(seq)+1)
    i,j=0,-1
    f[i]=j
    while i<len(seq):
        while j>=0 and seq[i]!=seq[j]:
            j=f[j]
        i+=1
        j+=1
        f[i]=j
    return f[1:]


if __name__=='__main__':
    print(datetime.datetime.now())
    infile,outfile=sys.argv[1],sys.argv[2]
    sequence=str(list(readfasta(infile).values())[0])
    failure=failure_array(sequence)
    print(failure)
    with open(outfile,'w') as whandle:
        whandle.write(' '.join([str(x) for x in failure]))
        whandle.write('\n')
    print(datetime.datetime.now())