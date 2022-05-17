graph={'5':['3','7'],'3':['2','4'],'7':['8'],'2':[],'4':['8'],'8':[]}
visite=set()
def dfs(visite,graph,node):
  if node not in visite:
    print(node)
    visite.add(node)
    for neighbour in graph[node]:
      dfs(visite,graph,neighbour)
dfs(visite,graph,'5')

visited=[]
queue=[]

def bfs(visited,graph,node1):
  visited.append(node1)
  queue.append(node1)
  while queue:
    m=queue.pop(0)
    print(m,end="")
    for j in graph[m]:
      if j not in visited:
        visited.append(j)
        queue.append(j)
bfs(visited,graph,'5')
