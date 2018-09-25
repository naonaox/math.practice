import sys
from Bio import SeqIO

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))

def gc_content(seq):
    SEQ=seq.upper()
    gcs=0.0
    for b in SEQ:
        if b in 'GC':
            gcs+=1
    return gcs/len(SEQ)

def highest_gc(id_seq_dict):
    gc_array=[(x,gc_content(id_seq_dict[x])) for x in id_seq_dict]
    gc_array.sort(key=lambda x:x[1])
    gc_array=list(reversed(gc_array))
    return gc_array[0]

infile=sys.argv[1]
outfile=sys.argv[2]
fastainfo=readfasta(infile)
highest=highest_gc(fastainfo)
output_str=highest[0]+'\n'+str(round(highest[1]*100,6))
with open(outfile,'w') as outf:
    outf.write(output_str+'\n')