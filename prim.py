# -*- coding: utf-8 -*-

'''

    Associate with each vertex v of the graph a number C[v] (the cheapest
    cost of a connection to v) and an edge E[v] (the edge providing that
    cheapest connection). To initialize these values, set all values of C[v]
    to +∞ (or to any number larger than the maximum edge weight) and set
    each E[v] to a special flag value indicating that there is no edge
    connecting v to earlier vertices.
    
    Initialize an empty forest F and a set Q of vertices that have not yet
    been included in F (initially, all vertices).
    
    Repeat the following steps until Q is empty:
        Find and remove a vertex v from Q having the minimum possible value
        of C[v]
        Add v to F and, if E[v] is not the special flag value, also add E[v]
        to F
        Loop over the edges vw connecting v to other vertices w. For each
        such edge, if w still belongs to Q and vw has smaller weight than
        C[w], perform the following steps:
            Set C[w] to the cost of edge vw
            Set E[w] to point to edge vw.
            
    Return F

'''

nodes=[1,2,3,4,5]
#g=[[1,2,11],[2,3,4],[4,5,6],[1,3,2],[3,5,10]]

g=[[1, 2, 24],
[1, 4, 20],
[3, 1, 3],
[4, 3, 12]]

g=[[1, 2, 3],
[1, 3, 4],
[4, 2, 6],
[5, 2, 2],
[2, 3, 5],
[3, 5, 7]]

def graph(g,node):
    ret=set()
    for i in g:
        if i[0]==node:
            ret.add(i[1])
        if i[1]==node:
            ret.add(i[0])
    return list(ret)
    
def leng(g,u,v):
    for i in g:
        if [u,v]==i[0:2] or [v,u]==i[0:2]:
            return i[2]
    return 10**9


def prim(g,nodes,inf=10**9):
    c={}
    e={}
    for n in nodes:
        c[n]=inf
        e[n]=None

    q=nodes
    f=[]
    while len(q)>0:
        minc=inf+1
        for i in q:
            if c[i]<minc:
                minc=c[i]
                v=i
        q.remove(v)
        f.append(v)
        if e[v]<>None:
            f.append(e[v])
        for w in graph(g,v):
            if w in q and leng(g,v,w)<c[w]:
                c[w]=leng(g,v,w)
                e[w]=[v,w]
    return f

p=prim(g,nodes)
su=0
for i in p:
    if type(i)==list:
        su+=leng(g,i[0],i[1])
print su
            
        
