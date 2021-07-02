def bfs(graph, start, size):
  queue = [start]
  while len(queue) > 0:
    curR, curC = queue.pop(0)
    sur = getSurrounding(curR, curC, size[0], size[1])
    
def getSurrounding(posX, posY, maxX, maxY):
  sur = []
  if posX == 0:
    sur.append((posX + 1, posY))
  elif posX == maxX:
    sur.append((posX - 1, posY))
  else:
    sur.append((posX + 1, posY))
    sur.append((posX - 1, posY))
  if posY == 0:
    sur.append((posX, posY + 1))
  elif posY == maxY:
    sur.append((posX, posY - 1))
  else:
    sur.append((posX, posY - 1))
    sur.append((posX, posY + 1))
  return sur
r, c = map(int, input().split())
while r != 0 and c != 0:
  n = int(input())
  bombMap = [[] for _ in range(n)]
  for i in range(n):
    bombMap[i] = list(map(int, input().split()))
  startR, startC = map(int, input().split())
  endR, endC = map(int, input().split())
