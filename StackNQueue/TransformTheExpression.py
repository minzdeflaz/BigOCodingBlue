n = int(input())
inpList = []
for i in range(n):
  inpList.append(input())
def solve(inp):
  cout = ''
  stack = []
  for i in inp:
    if i.isalpha():
      cout += i
    elif i in ['*', '-', '+', '/','^']:
      stack.append(i)
    elif i == ')':
      cout += stack.pop()
  return cout
for i in inpList:
  print(solve(i))