# Source: https://codeforces.com/problemset/problem/572/A

NA, NB = tuple(map(int,input().split()))
K, M = tuple(map(int,input().split()))
listNA = list(map(int,input().split()))
listNB = list(map(int,input().split()))
if listNA[K - 1] < listNB[NB -M]:
  print("YES")
else:
  print("NO")