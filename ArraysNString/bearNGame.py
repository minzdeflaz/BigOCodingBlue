# Source: https://codeforces.com/problemset/problem/673/A

n = int(input())
inNums = list(map(int, input().split()))
cur = 0
for i in range(n):
  if inNums[i] - cur > 15:
    break
  cur = inNums[i]
if cur + 15 > 90:
  print(90)
else:
  print(cur + 15)