def find(sett, item):
    next = sett[item]
    while next != -1:
        item = next
        next = sett[item]
    return item
def merge(sett, i ,j):
    lead1 = find(sett, i)
    lead2 = find(sett, j)
    if lead1 == j or lead2 == i:
        return
    sett[lead1] = lead2
def solve(n, m, num):
    sett = {i: -1 for i in range(1, n + 1)}
    for _ in range(m):
        i, j = map(int, input().split())
        merge(sett, i, j)
    count = 0
    for i in sett.keys():
        if sett[i] == -1:
            count += 1
    print(f'Case {num}: {count}')

if __name__ == '__main__':
    num = 1
    n, m = map(int, input().split())
    while n != 0 and m != 0:
        solve(n, m, num)
        num += 1
        n, m = map(int, input().split())
