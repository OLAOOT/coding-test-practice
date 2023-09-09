import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
tri, dp = [[0]], [[0]]
for i in range(n):
    tri.append(list(map(int, input().split())))
    dp.append([0] * (i + 1))

for i in range(1, n + 1):
    for j in range(i):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + tri[i][j]
        elif j == i - 1:
            dp[i][j] = dp[i - 1][j - 1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i][j]
            
print(max(dp[-1]))