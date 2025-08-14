import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(sx, sy, visited):
    q = deque([(sx, sy)])
    union = [(sx, sy)]
    visited[sx][sy] = True
    total = graph[sx][sy]

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny))
                    total += graph[nx][ny]
    return union, total

cnt = 0
while True:
    visited = [[False] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union, total = bfs(i, j, visited)
                if len(union) > 1:
                    moved = True
                    new_pop = total // len(union)
                    for x, y in union:
                        graph[x][y] = new_pop
    if not moved:
        break
    cnt += 1

print(cnt)
