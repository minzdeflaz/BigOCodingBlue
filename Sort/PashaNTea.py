n, w = tuple(map(int,input().split()))
nums = list(map(int,input().split()))
nums.sort()
if nums[0] * 2 <= nums[n]:
  total = nums[0]*3*n
else:
  total = nums[n]*3/2*n
if total > w:
  total = w
if total == round(total):
  print(round(total))
else:
  print(total)