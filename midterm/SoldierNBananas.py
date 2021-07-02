k, n, w = map(int, input().split())
moneyNeeded = 0
for i in range(w):
  moneyNeeded += k * (i + 1)
if moneyNeeded < n:
  print(0)
else:
  print(moneyNeeded - n)