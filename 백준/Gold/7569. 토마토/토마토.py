import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

from collections import deque

m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]
q = deque([])

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k, 0))

dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

answer = 0

while q:
    x, y, z, day = q.popleft()
    nday = day + 1
    for d in range(6):
        nx, ny, nz = x + dx[d], y + dy[d], z + dz[d]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and \
            graph[nx][ny][nz] == 0:
            graph[nx][ny][nz] = 1
            q.append((nx, ny, nz, nday))
            answer = nday

def print_ans():
    for i in range(h):
        for j in range(n):
            if 0 in graph[i][j]:
                print(-1)
                return
    print(answer)

print_ans()