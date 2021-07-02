class Node:
    def __init__(self):
        self.countNum = 0
        self.child = {}



def addNum(root, string):
    cur = root
    for char in string:
        if char not in cur.child:
            cur.child[char] = Node()
        cur = cur.child[char]
    cur.countNum += 1


t = int(input())
for _ in range(t):
    n = int(input())
    root = Node()
    for _ in range(n):
        addNum(root, input())
    print(root.child)
    # if len(root) < n:
    #     print('YES')
    # else:
    #     print('NO')
