#Enumerating k-mers Lexicographically

import sys
from itertools import product

if __name__=='__main__':
    infile=sys.argv[1]
    outfile=sys.argv[2]

    with open(infile) as rhandle:
        rreads=rhandle.read().split('\n')
        alphabets,perm=rreads[0].split(' '),int(rreads[1])

    lexorder=list(product(alphabets,repeat=perm))
    with open(outfile,'w') as whandle:
        for item in lexorder:
            for i in range(len(item)):
                if i!=len(item)-1:
                    whandle.write(item[i])
                else:
                    whandle.write(item[i]+'\n')