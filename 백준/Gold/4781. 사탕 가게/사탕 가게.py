import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

while True:
    n, money = input().split()
    n = int(n)
    money = int(money.replace('.', ''))
    if n == 0:
        break

    candies = [[0, 0]]
    for _ in range(n):
        c, p = input().split()
        candies.append([int(c), int(p.replace('.', ''))])

    dp = [0] * (money + 1)
    for c, p in candies:
        for i in range(p, money + 1):
            dp[i] = max(dp[i], dp[i - p] + c)
    print(dp[-1])