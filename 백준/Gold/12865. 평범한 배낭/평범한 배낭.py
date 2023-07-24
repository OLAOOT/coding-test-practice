import sys
# f = open('input.txt', 'r')
# input = f.readline
input = sys.stdin.readline

n, k = map(int, input().split())
package = []
for _ in range(n):
    package.append(tuple(map(int, input().split())))
package.sort()

dp = [[0] * (k + 1) for _ in range(n)]
for i in range(package[0][0], k + 1):
    dp[0][i] = package[0][1]

for i in range(1, n):
    for j in range(package[0][0], k + 1):
        if package[i][0] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - package[i][0]] + package[i][1])

print(dp[-1][-1])