import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
ps = list(map(int, input().split()))
d = int(input())

tree = [[] for _ in range(n)]
for i, p in enumerate(ps):
    if p == -1:
        root = i
    else:
        tree[p].append(i)

cnt = 0
def dfs(node):
    global cnt
    
    if not node:
        cnt += 1
        return

    for c in node:
        if c != d:
            dfs(tree[c])
        elif len(node) == 1:
            cnt += 1
            return

if root == d:
    print(0)
else:
    dfs(tree[root])
    print(cnt)