import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

r, c = map(int, input().split())
graph = [list(map(lambda n: n == '1', input().strip().split())) for _ in range(r)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
sx, sy = 0, 0
cnt = 0
cnt_cheese = lambda g: sum(sum(row) for row in g)
final_cheese = cnt_cheese(graph)
while True:
    new_graph = [row[:] for row in graph]
    visited = [[False] * c for _ in range(r)]
    visited[sx][sy] = True
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny]:
                    new_graph[nx][ny] = False
                else:
                    q.append((nx, ny))

    graph = [row[:] for row in new_graph]
    cnt += 1
    cheese = cnt_cheese(graph)
    if cheese == 0:
        print(cnt)
        print(final_cheese)
        break
    else:
        final_cheese = cheese