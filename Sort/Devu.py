n, x = tuple(map(int,input().split()))
nums = list(map(int, input().split()))
nums.sort()
total = 0
for i in nums:
    total += i * x
    if x > 1:
        x -= 1
print(total)