import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
dp = [[0] * n for _ in range(n)]
def dfs(x, y):
    global graph, dx, dy, dp

    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1) # 4방향

    return dp[x][y]

for i in range(n):
    for j in range(n):
        dfs(i, j)

print(max(max(row) for row in dp))