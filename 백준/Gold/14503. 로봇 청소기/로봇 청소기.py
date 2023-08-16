import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
cnt = 0

while True:
    if not visited[x][y]:
        visited[x][y] = True
        cnt += 1
    
    flag = False
    for i in range(4):
        d = d - 1 if d > 0 else 3
        if graph[x + dx[d]][y + dy[d]] == 0 and not visited[x + dx[d]][y + dy[d]]:
            flag = True
            break
    if flag:
        x, y = x + dx[d], y + dy[d]
        continue
    else:
        if graph[x - dx[d]][y - dy[d]] == 0:
            x, y = x - dx[d], y - dy[d]
        else:
            break

print(cnt)