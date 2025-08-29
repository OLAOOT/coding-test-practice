import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n, k = map(int, input().split())
graph = [[2] * (n + 2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(n)] + [[2] * (n + 2)]
pieces = [list(map(int, input().split())) for _ in range(k)]
cnt = 0
dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
dr = [0, 2, 1, 4, 3]
cur_g = [[[] for _ in range(n + 2)] for _ in range(n + 2)]
for i in range(k):
    cur_g[pieces[i][0]][pieces[i][1]].append(i)

def move(targets, x, y, nx, ny, i_idx):
    for target in targets:
        pieces[target][0] = nx
        pieces[target][1] = ny
    cur_g[x][y] = cur_g[x][y][:i_idx]
    if graph[nx][ny] == 1:
        targets.reverse()
    cur_g[nx][ny] += targets
    
for t in range(1, 1001):
    for i in range(k):
        x, y, d = pieces[i]
        nx, ny = x + dx[d], y + dy[d]
        i_idx = cur_g[x][y].index(i)
        targets = cur_g[x][y][i_idx:]

        if graph[nx][ny] in (0, 1):
            move(targets, x, y, nx, ny, i_idx)
        else:
            d = dr[d]
            pieces[i][2] = d
            nx, ny = x + dx[d], y + dy[d]

            if graph[nx][ny] in (0, 1):
                move(targets, x, y, nx, ny, i_idx)
                
        if len(cur_g[nx][ny]) >= 4:
            print(t)
            sys.exit()
else:
    print(-1)