# Source: https://codeforces.com/problemset/problem/242/B

N = int(input())
minn, maxx = tuple(map(int,input().split()))
minnList, maxxList = [minn], [maxx]
for i in range(1, N):
	data = tuple(map(int,input().split()))
	minnList.append(data[0])
	maxxList.append(data[1])
	if minn > data[0]:
		minn = data[0]
	if maxx < data[1]:
		maxx = data[1]
pos = -1
for i in range(N):
	if minnList[i] == minn and maxxList[i] == maxx:
		pos = i + 1
print(pos)