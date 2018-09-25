import sys

def stringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    return strs

def dna_to_rna(dnaseq):
    DNA=dnaseq.upper()
    RNA=DNA.replace('T','U')
    return RNA

infile=sys.argv[1]
outfile=sys.argv[2]

dnaseqs=stringRead(infile)
rnaseq=dna_to_rna(dnaseqs[0])

with open(outfile, 'w') as outf:
    outf.write(rnaseq+'\n')