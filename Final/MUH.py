def printPlans(repeat):
    seq = [[] for _ in range(3)]
    switch = 0
    for _, val in sorted(repeat.items()):
        if val[0] == 1:
            for arr in seq:
                arr.append(val[1])
        elif val[0] == 2:
            for arr in seq:
                if switch % 4:
                    arr.extend(val[1:3])
                    switch += 1
                else:
                    arr.extend(val[-1:0:-1])
                    switch += 1
        else:
            seq[0].extend(val[1:len(val) + 1])
            seq[1].extend(val[-1:0:-1])
            seq[2].append(val.pop())
            seq[2].extend(val[1:len(val) + 1])
    for arr in seq:
        print(*arr, sep=' ')

n = int(input())
nums = list(map(int, input().split()))
repeat = {}
for ite, val in enumerate(nums):
    if val in repeat.keys():
        repeat[val][0] += 1
        repeat[val].append(ite + 1)
    else:
        repeat[val] = [1, ite + 1]
count = 0
for val in repeat.values():
    if val[0] > 2:
        print('YES')
        printPlans(repeat)
        exit()
    elif val[0] == 2:
        count += 1
if count >= 2:
    print('YES')
    printPlans(repeat)
    exit()
print('NO')