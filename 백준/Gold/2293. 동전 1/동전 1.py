import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [1] + [0] * k

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[-1])