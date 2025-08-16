import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

def d(n): return (2 * n) % 10000
def s(n): return 9999 if n == 0 else n - 1
def l(n): return int(str(n).zfill(4)[1:] + str(n).zfill(4)[0])
def r(n): return int(str(n).zfill(4)[-1] + str(n).zfill(4)[:-1])

cmd_names = ['D', 'S', 'L', 'R']
funcs = [d, s, l, r]

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    visited = [False] * 10000
    prev = [-1] * 10000
    cmd = [''] * 10000

    q = deque([a])
    visited[a] = True

    while q:
        cur = q.popleft()
        if cur == b:
            break
        for i in range(4):
            nxt = funcs[i](cur)
            if not visited[nxt]:
                visited[nxt] = True
                prev[nxt] = cur
                cmd[nxt] = cmd_names[i]
                q.append(nxt)

    path = []
    cur = b
    while cur != a:
        path.append(cmd[cur])
        cur = prev[cur]
    print(''.join(reversed(path)))