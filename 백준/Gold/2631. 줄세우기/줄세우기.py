import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
children = [int(input()) for _ in range(n)]
dp = [1] * n
result = 1

for i in range(n):
    for j in range(i):
        if children[i] > children[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])

print(n - result)