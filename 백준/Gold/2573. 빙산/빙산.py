import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

def bfs():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    cnt = 0
    
    while True:
        cnt += 1
        new_graph = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if graph[i][j] != 0:
                    nxt_n = graph[i][j]
                    for d in range(4):
                        if graph[i + dx[d]][j + dy[d]] == 0:
                            nxt_n -= 1
                    new_graph[i][j] = nxt_n if nxt_n >= 0 else 0
                else:
                    new_graph[i][j] = 0

        start = (-1, -1)

        for i in range(n):
            for j in range(m):
                if new_graph[i][j] > 0:
                    start = (i, j)
                    break
        if start == (-1, -1):
            print(0)
            return

        q = deque([])
        visited = [[False] * m for _ in range(n)]

        q.append(start)
        visited[start[0]][start[1]] = True
        while q:
            x, y = q.popleft()
            for d in range(4):
                if not visited[x + dx[d]][y + dy[d]] and \
                new_graph[x + dx[d]][y + dy[d]] > 0:
                    visited[x + dx[d]][y + dy[d]] = True
                    q.append((x + dx[d], y + dy[d]))

        for i in range(n):
            for j in range(m):
                if new_graph[i][j] > 0 and not visited[i][j]:
                    print(cnt)
                    return

        graph = [r[:] for r in new_graph]

bfs()