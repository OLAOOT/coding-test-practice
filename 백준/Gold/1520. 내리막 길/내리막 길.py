import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

dp = [[-1] * c for _ in range(r)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def dfs(x, y):
    if x == r - 1 and y == c - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    global dx, dy
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] < graph[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))