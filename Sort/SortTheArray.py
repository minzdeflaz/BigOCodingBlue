n = int(input())
nums = list(map(int, input().split()))
numsCopy = nums.copy()
numsCopy.sort()
changes = []
pos = []
switch = True
i = 0
while i < n - 2:
  j = i + 1
  if nums[i] > nums[j]:
    changes.append(nums[i])
    pos.append(i)
    if len(changes) > 2:
        switch = False
        break
    while nums[i] > nums[j]:
        i += 1
        j += 1
        if j == n:
            break
    changes.append(nums[i])
    pos.append(i)
    i = j
  else:
    i += 1
if switch == True:
  if len(changes) == 0:
    print("yes") 
    print("1 1")
  else:
    nums[pos[0]: pos[1] + 1] = sorted(nums[pos[0]: pos[1] + 1])
    if nums != numsCopy:
      print("no")
    else:
      print("yes") 
      print(*[str(i + 1) for i in pos], sep=' ')
else:
  print("no")
