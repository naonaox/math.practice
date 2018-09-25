#Overlap Graphs
'''
Networks arise everywhere in the practical world, especially in biology. Networks are prevalent in popular applications such as modeling the spread of disease, but the extent of network applications spreads far beyond popular science. Our first question asks how to computationally model a network without actually needing to render a picture of the network.

First, some terminology: graph is the technical term for a network; a graph is made up of hubs called nodes (or vertices), pairs of which are connected via segments/curves called edges. If an edge connects nodes v and w, then it is denoted by v,w (or equivalently w,v).

an edge v,w is incident to nodes v and w; we say that v and w are adjacent to each other;
the degree of v is the number of edges incident to it;
a walk is an ordered collection of edges for which the ending node of one edge is the starting node of the next (e.g., {v1,v2}, {v2,v3}, {v3,v4}, etc.);
a path is a walk in which every node appears in at most two edges;
path length is the number of edges in the path;
a cycle is a path whose final node is equal to its first node (so that every node is incident to exactly two edges in the cycle); and
the distance between two vertices is the length of the shortest path connecting them.
Graph theory is the abstract mathematical study of graphs and their properties
'''

import sys
import itertools
from Bio import SeqIO

def readfasta(inpath):
    names,seqs=[],[]
    with open(inpath,'rU') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            names.append(record.id)
            seqs.append(record.seq)
    return dict(zip(names,seqs))

def overlap_strings(sequencedic,overlap_len=3):
    seqnames=sequencedic.keys()
    seqgroups=list(itertools.permutations(seqnames,2))
    overlapseq=[x for x in seqgroups if sequencedic[x[0]][-overlap_len:]==sequencedic[x[1]][:overlap_len]]
    return overlapseq

infile=sys.argv[1]
outfile=sys.argv[2]
inputsequences=readfasta(infile)

output_overlap=overlap_strings(inputsequences)
output_string='\n'.join([x[0]+' '+x[1] for x in output_overlap])
with open(outfile,'w') as handle:
    handle.write(output_string+'\n')