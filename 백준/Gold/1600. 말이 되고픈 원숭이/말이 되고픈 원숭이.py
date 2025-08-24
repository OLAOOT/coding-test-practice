import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

k = int(input())
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[[False for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
hdx, hdy = [1, 2, 2, 1, -1, -2, -2, -1], [2, 1, -1, -2, -2, -1, 1, 2]
q = deque([(0, 0, 0, 0)]) # x, y, horse count, moving count

while q:
    x, y, h_cnt, m_cnt = q.popleft()
    if x == n - 1 and y == m - 1:
        print(m_cnt)
        sys.exit()
    n_m_cnt = m_cnt + 1
    
    if h_cnt < k:
        n_h_cnt = h_cnt + 1
        for d in range(8):
            nx, ny = x + hdx[d], y + hdy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][n_h_cnt] and graph[nx][ny] == 0:
                visited[nx][ny][n_h_cnt] = True
                q.append((nx, ny, n_h_cnt, n_m_cnt))
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][h_cnt] and graph[nx][ny] == 0:
            visited[nx][ny][h_cnt] = True
            q.append((nx, ny, h_cnt, n_m_cnt))

print(-1)