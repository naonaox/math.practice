#Introduction to Random Strings

import sys,math

def common_log_strprob(seq,gc):
    sequpper=seq.upper()
    prob=(((1-gc)/2)**(sequpper.count('A')+sequpper.count('T')))*((gc/2)**(sequpper.count('C')+sequpper.count('G')))
    return math.log10(prob)

if __name__=='__main__':
    infile,outfile=sys.argv[1],sys.argv[2]
    with open(infile) as rhandle:
        lines=rhandle.read().split('\n')
        sequence=lines[0]
        gcs=[float(x) for x in lines[1].split(' ')]

    logprobs=[common_log_strprob(sequence,x) for x in gcs]
    with open(outfile,'w') as whandle:
        whandle.write(' '.join([str(round(x,6)) for x in logprobs])+'\n')