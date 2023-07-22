import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

from collections import deque

graph = []
q = deque([])

m, n = map(int, input().split())
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j, 0))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0
while q:
    x, y, day = q.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and \
        graph[nx][ny] == 0:
            graph[nx][ny] = 1
            q.append((nx, ny, day + 1))
    
    if not q:
        result = day

def print_result():
    for i in range(n):
        if 0 in graph[i]:
            print(-1)
            return
    print(result)

print_result()