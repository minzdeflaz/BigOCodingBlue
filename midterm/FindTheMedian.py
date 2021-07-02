n = int(input())
nums = list(map(int, input().split()))
nums.sort()
if n % 2:
  print(nums[int((n - 1) / 2)])
else:
  print((nums[int(n / 2)] + nums[int(n / 2) - 1]))