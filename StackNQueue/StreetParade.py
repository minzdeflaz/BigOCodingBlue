def solve(n):
  inp = list(map(int, input().split()))
  stack = []
  newOrder = []
  for i in range(1, n):
    if inp[i - 1] > inp[i]:
      stack.append(inp[i - 1])
    else:
      if len(newOrder) > 0 and len(stack) > 0:
        if newOrder[-1] < stack[-1] and inp[i - 1] > stack[-1]:
          newOrder.append(stack.pop())
        else:
          newOrder.append(inp[i - 1])
  
  if len(stack) == 0:
    return 'yes'
  else:
    return 'no'
n = int(input())
while n != 0:
  print(solve(n))
  n = int(input())

