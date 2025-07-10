import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    coins = list(map(int, input().split()))
    amount = int(input())

    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(1, amount + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
    print(dp[amount])