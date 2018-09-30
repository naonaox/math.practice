#Completing a Tree

import sys

def tree_complete(n,adjancency):
    subtrees=[set(adjancency[0])]
    intreeset=set(adjancency[0])
    for i in range(1,len(adjancency)):
        qualified_sets=[]
        intreeset.add(adjancency[i][0])
        intreeset.add(adjancency[i][1])
        for j in range(len(subtrees)):
            if adjancency[i][0] in subtrees[j] or adjancency[i][1] in subtrees[j]:
                qualified_sets.append(j)
        if len(qualified_sets)==1:
            newset=subtrees[qualified_sets[0]]
            newset.add(adjancency[i][0])
            newset.add(adjancency[i][1])
            subtrees=[subtrees[x] for x in range(len(subtrees)) if x!=qualified_sets[0]]
            subtrees.append(newset)
        elif len(qualified_sets)>1:
            newset=set()
            for k in qualified_sets:
                newset=newset|subtrees[k]
            newset.add(adjancency[i][0])
            newset.add(adjancency[i][1])
            subtrees=[subtrees[x] for x in range(len(subtrees)) if x not in qualified_sets]
            subtrees.append(newset)
        elif len(qualified_sets)==0:
            subtrees.append(set(adjancency[i]))
    untreed=[x for x in range(1,n+1) if x not in intreeset]
    for item in untreed:
        newset=set()
        newset.add(item)
        subtrees.append(newset)
    return len(subtrees)-1

if __name__=='__main__':
    infile,outfile=sys.argv[1],sys.argv[2]
    with open(infile) as rhandle:
        rlines=rhandle.read().split('\n')
        n=int(rlines[0])
        arrays=[[int(x) for x in y.split(' ')] for y in rlines[1:] if y!='']
    addedge=tree_complete(n,arrays)
    with open(outfile,'w') as whandle:
        whandle.write(str(addedge)+'\n')