# Source: https://codeforces.com/problemset/problem/518/A

inp1 = input()
inp2 = input()
temp = ''
pos = 0
for i in range(len(inp1) - 1, -1, -1):
  pos = i
  if inp1[i] != 'z':
    temp += chr(ord(inp1[i]) + 1)
    break
  temp += 'a'
result = inp1[:pos] + temp[::-1]
if result < inp2:
  print(result)
else:
  print('No such string')