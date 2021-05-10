n = int(input())
rating = list(map(int,input().split()))
count = {}
for i in rating:
  if i not in count:
    count[i] = 1
  else:
    count[i] += 1
newRate = {}
stack = 0
for i in sorted(count,reverse=True):
  newRate[i] = 1 + stack
  stack += count[i]
for i in range(len(rating)):
  rating[i] = newRate[rating[i]]
print(*rating,sep=' ')