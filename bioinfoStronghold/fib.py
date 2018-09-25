import sys

def numberstringRead(inpath):
    with open(inpath) as infile:
        strs = infile.read().split('\n')
    str0=strs[0]
    nums=[int(x) for x in str0.split(' ')]
    return nums

def wascallyRab(month,pair):
    mature_rab=[0,1]
    baby_rab=[1,0]
    for i in range(2,month):
        #mature_rab[i]=
        mature_rab.append(mature_rab[i-1]+baby_rab[i-1])
        #baby_rab[i]=
        baby_rab.append(mature_rab[i-1]*pair)
    return mature_rab[month-1]+baby_rab[month-1]

infile=sys.argv[1]
outfile=sys.argv[2]

readfile=numberstringRead(infile)
n=readfile[0]
k=readfile[1]
rab_num=wascallyRab(n,k)
with open(outfile,'w') as outf:
    outf.write(str(rab_num)+'\n')