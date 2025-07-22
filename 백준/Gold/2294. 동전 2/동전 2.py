import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] + [int(1e6)] * k
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[-1]) if dp[-1] != int(1e6) else print(-1)