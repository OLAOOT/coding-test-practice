import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

land_num = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            q = deque([(i, j)])
            graph[i][j] = land_num
            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                        graph[nx][ny] = land_num
                        q.append((nx, ny))
            land_num += 1

visited = [[False] * n for _ in range(n)]
beaches = set()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] != 0:
                            beaches.add((x, y, graph[nx][ny]))
                        elif graph[nx][ny] == 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

def bfs(bx, by, land):
    global dx, dy, graph
    q = deque([(bx, by, 1)])
    
    visited = [[False] * n for _ in range(n)]
    visited[bx][by] = True
    while q:
        x, y, dist = q.popleft()
        ndist = dist + 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] not in (0, land):
                    return dist
                elif graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, ndist))
    return 10000

result = 10000
for bx, by, land in beaches:
    result = min(result, bfs(bx, by, land))

print(result)