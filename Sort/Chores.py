n, a, b = tuple(map(int,input().split()))
chores = list(map(int,input().split()))
chores.sort()
print(chores[b] - chores[b-1])
