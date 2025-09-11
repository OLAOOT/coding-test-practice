import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
ms = [list(map(int, input().split())) for _ in range(n)]
if n == 1:
    print(0)
    sys.exit()
if n == 2:
    print(ms[0][0] * ms[0][1] * ms[1][1])
    sys.exit()

dp = [[2 ** 32] * n for _ in range(n)]
for i in range(n - 1):
    dp[i][i] = 0
    dp[i][i + 1] = ms[i][0] * ms[i][1] * ms[i + 1][1]
dp[n - 1][n - 1] = 0

for i in range(2, n):
    for j in range(n - i):
        for k in range(j, j + i): 
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + ms[j][0] * ms[k][1] * ms[j + i][1])

print(dp[0][-1])