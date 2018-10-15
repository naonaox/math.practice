#Ordering Strings of Varying Length Lexicographically

import sys


def vary_length_lexi(chars,n):
    nums=range(1,len(chars)+1)
    str=[0]*n
    str_collections=[]
    while str!=[len(chars)]*n:
        nonzero_len=str.count(0)
        if nonzero_len!=0:
            str[-1*nonzero_len]=nums[0]
        else:
            if str[-1]!=nums[-1]:
                str[-1]+=1
            else:
                for i in range(n-1,-1,-1):
                    if str[i]!=nums[-1]:
                        str[i]+=1
                        for j in range(i+1,n):
                            str[j]=0
                        break
        str_collections.append(str.copy())
    position_collection=[]
    for item in str_collections:
        new_item=[x-1 for x in item if x!=0]
        new_str=''.join([chars[x] for x in new_item])
        position_collection.append(new_str)
    return position_collection

if __name__=='__main__':
    infile,outfile=sys.argv[1],sys.argv[2]
    chas,lexlen=[],0
    with open(infile) as rhandle:
        records=rhandle.read().split('\n')
        chas=records[0].split(' ')
        lexlen=int(records[1])
    outlex=vary_length_lexi(chas,lexlen)
    with open(outfile,'w') as whandle:
        for i in outlex:
            whandle.write(i+'\n')