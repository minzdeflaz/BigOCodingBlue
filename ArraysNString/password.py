# Source: https://codeforces.com/problemset/problem/721/B
n, k = map(int, input().split())
tries = []
for _ in range(n):
    tries.append(input())
pw = input()
countSmall = 0
countSmallNEqual = 0
for i in tries:
    if len(i) < len(pw):
        countSmall += 1
        countSmallNEqual += 1
    elif len(i) == len(pw):
        countSmallNEqual +=1
worst = countSmallNEqual//k*5 + countSmallNEqual
best = countSmall//k*5 + countSmall + 1
print(best, worst) 