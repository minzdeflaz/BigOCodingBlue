import heapq
n = int(input())
if n < 3:
    for _ in range(n):
        print(-1)
    exit()
nums = list(map(int, input().split()))
largest = []
for i in range(3):
    heapq.heappush(largest,nums[i])
print(-1, -1, sep='\n')
print(largest[0] * largest[1] * largest[2])
for i in range(3, n):
    if nums[i] > largest[0]:
        heapq.heappushpop(largest, nums[i])
    print(largest[0] * largest[1] * largest[2])