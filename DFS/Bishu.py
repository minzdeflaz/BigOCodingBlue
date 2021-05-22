n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
  x, y = map(int, input().split())
  graph[x - 1].append(y - 1)
  graph[y - 1].append(x - 1)
q = int(input())
locations = []
for _ in range(q):
  locations.append(int(input()) - 1)
def bfs (start, graph, vNums):
  stack = [start]
  path = [0]
  path.extend([-1] * (vNums - 1))
  while len(stack) != 0:
    cur = stack.pop()
    if len(graph[cur]) != 0:
      for i in graph[cur]:
        if path[i] == -1:
          stack.append(i)
          path[i] = path[cur] + 1
  return path
path = bfs(0, graph, n)
minID = locations[0]
minDis = path[minID]
for i in range(2,len(locations)):
  if minDis > path[locations[i]]:
    minDis = path[locations[i]]
    minID = locations[i]
  elif minDis == path[locations[i]]:
    if minID > locations[i]:
      minID = locations[i]
print(minID + 1)