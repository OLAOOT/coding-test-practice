import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
if n % 2 == 1:
    print(0)
elif n == 2:
    print(3)
else:
    dp = [0] * (n + 1)
    dp[2] = 3

    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + sum(dp[2:i - 3:2]) * 2 + 2
    print(dp[-1])
