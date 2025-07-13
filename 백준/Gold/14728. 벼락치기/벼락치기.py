import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n, time = map(int, input().split())
chapters = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (time + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, time + 1):
        if j < chapters[i][0]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - chapters[i][0]] + chapters[i][1])

print(dp[n][time])