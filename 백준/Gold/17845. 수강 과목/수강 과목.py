import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

time, n = map(int, input().split())

lecs = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (time + 1)

for l, t in lecs:
    for i in range(time, t- 1, -1):
        dp[i] = max(dp[i], dp[i - t] + l)

print(dp[-1])