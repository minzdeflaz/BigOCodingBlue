q = int(input())
def solve():
  u, v = tuple(map(int,input().split()))
  graph = [[] * u]
  for i in range(v):
    v1, v2 = tuple(map(int, input().split()))
    graph[v1 - 1].append(v2 - 1)
    graph[v2 - 1].append(v1 - 1)
def bfs (graph, u, start):
  path = [-1] * u
  for i in graph[start]:
    
    while len(i) > 0:

    
for i in range(q):
  print(solve())