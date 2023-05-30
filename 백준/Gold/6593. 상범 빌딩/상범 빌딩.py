import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

def bfs(start):
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    q = deque([start])
    
    while q:
        x, y, z, cnt = q.popleft()
        for d in range(6):
            nx, ny, nz = x + dx[d], y + dy[d], z + dz[d]
            if 0 <= nx < l and 0 <= ny < r and \
            0 <= nz < c and not visited[nx][ny][nz] and graph[nx][ny][nz] != '#':
                if graph[nx][ny][nz] == 'E':
                    print(f'Escaped in {cnt + 1} minute(s).')
                    return
                visited[nx][ny][nz] = True
                q.append((nx, ny, nz, cnt + 1))
    print('Trapped!')

while True:
    l, r, c = map(int, input().split())
    if l == 0:
        break
    
    graph = []
    for i in range(l):
        floor = []
        for j in range(r):
            row = list(input().strip())
            floor.append(row)
            if 'S' in row:
                start = (i, j, row.index('S'), 0)
        graph.append(floor)
        input()

    bfs(start)