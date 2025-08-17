import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

def expand_water():
    global graph, latest, dx, dy
    new_latest = []
    for wx, wy in latest:
        for d in range(4):
            nx, ny = wx + dx[d], wy + dy[d]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] in ['.', 'S']:
                graph[nx][ny] = '*'
                new_latest.append((nx, ny))
    latest = new_latest[:]

def bfs(q):
    global graph, visited, dx, dy
    new_q = deque()

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] in ['.', 'D'] and not visited[nx][ny]:
                if graph[nx][ny] == 'D':
                    return True
                new_q.append((nx, ny))
                visited[nx][ny] = True
    return new_q

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
latest = []
for x in range(r):
    for y in range(c):
        if graph[x][y] == '*':
            latest.append((x, y))
        elif graph[x][y] == 'S':
            sx, sy = x, y
            visited[sx][sy] = True

time = 0
q = deque([(sx, sy)])
while True:
    time += 1
    expand_water()
    result = bfs(q)

    if result == True:
        print(time)
        break
    elif not result:
        print('KAKTUS')
        break
    else:
        q = deque(result) # 깊은복사