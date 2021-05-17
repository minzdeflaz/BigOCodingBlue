q = int(input())
def bfs (graph, u, start):
  path = [-1] * u
  path[start] = 0
  queue = [start]
  while len(queue) != 0:
    cur = queue.pop(0)
    for i in graph[cur]:
      if path[i] == -1:
        queue.append(i)
        path[i] = path[cur] + 6
  return path
def solve():
  u, v = map(int,input().split())
  graph = [[] for _ in range(u)]
  for _ in range(v):
    v1, v2 = map(int, input().split())
    graph[v1 - 1].append(v2 - 1)
    graph[v2 - 1].append(v1 - 1)
  start = int(input()) - 1
  path = bfs(graph, u, start)
  path.pop(start)
  print(*path, sep=' ')
for _ in range(q):
  solve()