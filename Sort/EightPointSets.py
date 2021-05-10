def solve ():
  nums = []
  for i in range(8):
    num = tuple(map(int,input().split()))
    nums.append(num)
  repeatI, repeatJ = [], []
  for i in nums:
    if i[0] not in repeatI:
      repeatI.append(i[0])
    if i[1] not in repeatJ:
      repeatJ.append(i[1])
    if len(repeatI) > 3 or len(repeatJ) > 3:
      return False
  repeatI.sort()
  repeatJ.sort()
  for i in repeatI:
    for j in repeatJ:
      if repeatI[1] == i and repeatJ[1] == j:
        continue
      if (i, j) not in nums:
        return False
  return True
if solve() == True:
  print('respectable')
else:
  print('ugly')