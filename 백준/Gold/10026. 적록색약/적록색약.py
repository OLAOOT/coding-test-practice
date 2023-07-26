import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
cnt = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            q = deque([(i, j)])
            cnt += 1
            while q:
                x, y = q.popleft()
                for d in range(4):
                    if 0 <= x + dx[d] < n and 0 <= y + dy[d] < n and not visited[x + dx[d]][y + dy[d]] and \
                    graph[x][y] == graph[x + dx[d]][y + dy[d]]:
                        visited[x + dx[d]][y + dy[d]] = True
                        q.append((x + dx[d], y + dy[d]))
print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
visited = [[False] * n for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            q = deque([(i, j)])
            cnt += 1
            while q:
                x, y = q.popleft()
                for d in range(4):
                    if 0 <= x + dx[d] < n and 0 <= y + dy[d] < n and not visited[x + dx[d]][y + dy[d]] and \
                    graph[x][y] == graph[x + dx[d]][y + dy[d]]:
                        visited[x + dx[d]][y + dy[d]] = True
                        q.append((x + dx[d], y + dy[d]))
                        
print(cnt)