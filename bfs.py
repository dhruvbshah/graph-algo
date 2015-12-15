

'''
1 Breadth-First-Search(Graph, root):
 2 
 3     for each node n in Graph:            
 4         n.distance = INFINITY        
 5         n.parent = NIL
 6 
 7     create empty queue Q      
 8 
 9     root.distance = 0
10     Q.enqueue(root)                      
11 
12     while Q is not empty:        
13     
14         current = Q.dequeue()
15     
16         for each node n that is adjacent to current:
17             if n.distance == INFINITY:
18                 n.distance = current.distance + 1
19                 n.parent = current
20                 Q.enqueue(n)
'''

nodes=[1,2,3,4,5]
g=[[1,2],[2,3],[3,5],[4,5]]

#for a node return connected nodes
def graph(g,node):
    ret=set()
    for i in g:
        if i[0]==node:
            ret.add(i[1])
        if i[1]==node:
            ret.add(i[0])
    return list(ret)
    
def bfs(g,nodes,root,inf=10**9):
    ret={}
    for node in nodes:
        ret[node]=[inf,None] #dist parent
    q=[]
    ret[root][0]=0
    q.append(root)
    while len(q)>0:
        cur=q.pop(0)
        for n in graph(g,cur):
            if ret[n][0]==inf:
                ret[n][0]=ret[cur][0]+1
                ret[n][1]=cur
                q.append(n)
    return ret

b=bfs(g,nodes,1)
print b
        
