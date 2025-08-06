import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n, m = map(int, input().split())
rs = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    rs[u].append(v)
    rs[v].append(u)

def dfs(node, visited):
    if len(visited) == 5:
        print(1)
        sys.exit()
    for n in rs[node]:
        if n not in visited:
            dfs(n, visited + [n])

for i in range(n):
    dfs(i, [i])
print(0)