
'''
void dfs(int node)  {
  seen[node] = true;
  for(int next: graph[node])  {
    if(not seen[next])  {
      dfs(next);
    }
  }
}
'''

seen=[]
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

def dfs(g,node):
    seen.append(node)
    #print node
    for n in graph(g,node):
        if n not in seen:
            dfs(g,n)

dfs(g,1)
print seen
        
    
