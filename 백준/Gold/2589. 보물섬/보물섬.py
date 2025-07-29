import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

n, m = map(int, input().split())

graph = [input().strip() for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def find_furthest(sx, sy):
    dist = [[-1] * m for _ in range(n)]
    dist[sx][sy] = 0
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()
        nd = dist[x][y] + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L' and dist[nx][ny] == -1:
                dist[nx][ny] = nd
                q.append((nx, ny))
    return max(max(row) for row in dist)

results = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            results.append(find_furthest(i, j))

print(max(results))