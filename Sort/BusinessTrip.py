k = int(input())
nums = list(map(int,input().split()))
nums.sort(reverse=True)
total, count = 0, 0
for i in nums:
  if total >= k:
    break
  total += i
  count += 1
if total < k:
  print(-1)
else:
  print(count)
