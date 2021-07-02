# Source: https://codeforces.com/problemset/problem/448/B

def solve (inp1, inp2):
  i, j = 0, 0
  while len(inp1) != i and len(inp1) != j:
    if inp1[j] != inp2[i]:
      j += 1
    i += 1
    j += 1
  else:
    return (True, False)
  
  ar = False
  cou1, cou2 = {}, {}
  for i in inp1:
    if i not in cou1:
      cou1[i] = 1
    else:
      cou1[i] +=1
  for i in inp2:
    if i not in cou2:
      cou2[i] = 1 
    else:
      cou2[i] +=1
  for i in cou2:
    if i in cou1:
      if cou2[i] <= cou2[i]:
        ar = True
        continue
    ar = False
    break
  if ar == True:
    if len(inp1) > len(inp2):
      return (True, True)
    else:
      return (False, True)
  return (False,False)
inp1, inp2 = input(), input()
au, ar = solve(inp1, inp2)
if au == True:
  if ar == True:
    print("both")
  else:
    print("automaton")
else:
  if ar == True:
    print("array")
  else:
    print("need tree")