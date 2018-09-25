from collections import defaultdict

def baseCount_dna(dnaseq):
    basedic=defaultdict(int)
    DNA=dnaseq.upper()
    for b in DNA:
        if b in 'ACTG':
            basedic[b]+=1
    return basedic