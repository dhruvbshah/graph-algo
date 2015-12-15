# -*- coding: utf-8 -*-

'''
1 let dist be a |V| × |V| array of minimum distances initialized to
    ∞ (infinity)
2 for each vertex v
3    dist[v][v] ← 0
4 for each edge (u,v)
5    dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
6 for k from 1 to |V|
7    for i from 1 to |V|
8       for j from 1 to |V|
9          if dist[i][j] > dist[i][k] + dist[k][j] 
10             dist[i][j] ← dist[i][k] + dist[k][j]
11         end if
'''

g=[[1, 2, 24],
[1, 4, 20],
[3, 1, 3],
[4, 3, 12]]

g=[[1, 2, 5],
[1, 4, 24],
[2, 4, 6],
[3, 4, 4],
[3, 2, 7]]

nodes=[1,2,3,4]

def floyd(g,nodes,inf=10**9):
    dist={}
    for n1 in nodes:
        dist[n1]={}
        for n2 in nodes:
            if n1==n2: v=0
            else: v=inf
            dist[n1][n2]=v
    for u,v,w in g:
        dist[u][v]=w
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


print floyd(g,nodes)  
    
            
    
