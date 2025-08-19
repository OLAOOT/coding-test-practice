import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

s, d = map(int, input().split())

visited = [False] * 100001
prev = [-1] * 100001
visited[s] = True
prev[s] = s
q = deque([s])

while q:
    cur = q.popleft()
    if cur == d:
        break
    nxt = cur + 1
    if nxt <= 100000 and not visited[nxt]:
        visited[nxt] = True
        q.append(nxt)
        prev[nxt] = cur
    nxt = cur - 1
    if nxt >= 0 and not visited[nxt]:
        visited[nxt] = True
        q.append(nxt)
        prev[nxt] = cur
    nxt = cur * 2
    if nxt <= 100000 and not visited[nxt]:
        visited[nxt] = True
        q.append(nxt)
        prev[nxt] = cur

bt = d
result = [bt]
while bt != s:
    bt = prev[bt]
    result.append(bt)
print(len(result) - 1)
print(' '.join(map(str, reversed(result))))