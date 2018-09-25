#Mendal's First Law

import sys,math

def numberstringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    str0=strs[0]
    nums=[int(x) for x in str0.split(' ')]
    return nums

def C(n,k):
    '''pick k elements from n elements'''
    Cnk=float(math.factorial(n))/((math.factorial(k))*(math.factorial(n-k)))
    return Cnk

def mendals_law(AA,Aa,aa):
    '''return outsprints probabilities of AA,Aa,aa'''
    total=AA+Aa+aa
    total_comb=C(total,2)
    P_AA2,P_Aa2,P_aa2=C(AA,2)/total_comb,C(Aa,2)/total_comb,C(aa,2)/total_comb
    P_AA_Aa,P_AA_aa,P_Aa_aa=C(AA,1)*C(Aa,1)/total_comb,C(AA,1)*C(aa,1)/total_comb,C(Aa,1)*C(aa,1)/total_comb
    outAA=P_AA_Aa*(1/2)+P_AA2+P_Aa2*(1/2)*(1/2)
    outAa=P_AA_Aa*(1/2)+P_AA_aa+P_Aa_aa*(1/2)+P_Aa2*((1/2)*(1/2)+(1/2)*(1/2))
    outaa=P_Aa2*(1/2)*(1/2)+P_aa2+P_Aa_aa*(1/2)
    return outAA,outAa,outaa

if __name__=='__main__':
    infile=sys.argv[1]
    outfile=sys.argv[2]

    readfile=numberstringRead(infile)
    k,m,n=readfile[0],readfile[1],readfile[2]
    AAprob,Aaprob,aaprob=mendals_law(k,m,n)
    outprob=AAprob+Aaprob
    with open(outfile,'w') as outf:
        outf.write(str(round(outprob,6))+'\n')