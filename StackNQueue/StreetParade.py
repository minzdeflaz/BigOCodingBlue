n = int(input())
nums = list(map(int, input().split()))
input()
def solve(inp):
  stack = []
  i = 1
  while i < len(inp):
    print(inp, i)
    if inp[i - 1] > inp[i]:
      stack.append(inp[i - 1])
      inp.pop(i - 1)
      continue
    elif len(stack) > 0:
      if inp[i - 1] < stack[-1] and inp[i] > stack[-1]:
        inp.append(stack.pop())
        continue
    i += 1

  if len(stack) == 0:
    return 'yes'
  else:
    return 'no'
print(solve(nums))