n = int(input())
nums = list(map(int,input().split()))
count = {}
maxx = 1
for i in nums:
  if i not in count:
    count[i] = 1
  else:
    count[i] += 1
  if count[i] > maxx:
    maxx = count[i]
print(maxx, len(count))