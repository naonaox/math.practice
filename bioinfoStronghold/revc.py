import sys

def stringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    return strs

def reverse_complement(dnastr):
    DNA=dnastr.upper()
    rev_dic={'A':'T','T':'A','C':'G','G':'C'}
    revcom_str=''
    for b in DNA:
        if b in rev_dic:
            revcom_str=rev_dic[b]+revcom_str
        else:
            revcom_str=b+revcom_str
    return revcom_str

infile=sys.argv[1]
outfile=sys.argv[2]

dnaseqs=stringRead(infile)
rev_complement=reverse_complement(dnaseqs[0])

with open(outfile, 'w') as outf:
    outf.write(rev_complement+'\n')