import heapq

num = int(input())
for _ in range(num):
  n, m = map(int,input().split())
  queue = list(map(int,input().split()))
  heap = [i * -1 for i in queue]
  heapq.heapify(heap)
  time = 1
  i = 0
  count = 0
  while True:
    cur = heapq.heappop(heap) * -1
    if i == m:
      print(time)
      break
    if cur > queue[i]:
      queue.append(queue.pop(0))
      queue.remove(cur)
      time += 1
      if i == m:
        m = len(queue)
      else:
        m -= 1
      count +=1
    else:
      i += 1
    if i == m:
      print(time)
      break