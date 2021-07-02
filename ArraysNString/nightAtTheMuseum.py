# Source: https://codeforces.com/problemset/problem/731/A

inp = input()
pos = 97
count = 0
for i in inp:
  nextPos = ord(i)
  if abs(nextPos - pos) > 26 - abs(nextPos - pos):
    count += 26 - abs(nextPos - pos)
  else: 
    count += abs(nextPos - pos)
  pos = nextPos
print(count)