# -*- coding: utf-8 -*-

'''
1  function Dijkstra(Graph, source):
 2
 3      create vertex set Q
 4
 5      for each vertex v in Graph:             // Initialization
 6          dist[v] ← INFINITY                  // Unknown distance from source to v
 7          prev[v] ← UNDEFINED                 // Previous node in optimal path from source
 8          add v to Q                          // All nodes initially in Q (unvisited nodes)
 9
10      dist[source] ← 0                        // Distance from source to source
11      
12      while Q is not empty:
13          u ← vertex in Q with min dist[u]    // Source node will be selected first
14          remove u from Q 
15          
16          for each neighbor v of u:           // where v is still in Q.
17              alt ← dist[u] + length(u, v)
18              if alt < dist[v]:               // A shorter path to v has been found
19                  dist[v] ← alt 
20                  prev[v] ← u 
21
22      return dist[], prev[]

node=vertex
'''

nodes=[1,2,3,4]
#g=[[1,2,11],[2,3,4],[4,5,6],[1,3,2],[3,5,10]]

g=[[1, 2, 24],
[1, 4, 20],
[3, 1, 3],
[4, 3, 12]]

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

def dijkstra(g,nodes,source,inf=10**9):
    q=[]
    dist={}
    prev={}
    for n in nodes:
        dist[n]=inf
        prev[n]=None
        q.append(n)

    dist[source]=0
    
    while len(q)>0:
        mindist=inf+1
        for i in q:
            if dist[i]<mindist:
                mindist=dist[i]
                u=i
        
        q.remove(u)
        for v in graph(g,u):
            #print dist[u],leng(g,u,v)
            alt=dist[u]+leng(g,u,v)
            if alt<dist[v]:
                dist[v]=alt
                prev[v]=u
    return dist, prev

print dijkstra(g,nodes,1)
