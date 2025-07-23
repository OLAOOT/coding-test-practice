import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0] = [v for v in graph[0]]
result = 1 if 1 in graph[0] else 0

for i in range(1, n):
    for j in range(m):
        if graph[i][j] == 0:
            dp[i][j] = 0
        elif j == 0:
            dp[i][j] = graph[i][j]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        result = max(result, dp[i][j])

print(result ** 2)