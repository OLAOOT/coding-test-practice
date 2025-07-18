import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
works = [list(map(int, input().split())) for _ in range(n)]
sum_a = sum(work[0] for work in works)

dp = [int(1e6)] * (sum_a + 1)
dp[0] = 0

for a, b in works:
    for i in range(sum_a, a - 1, -1):
        dp[i] = min(dp[i], dp[i - a] + b)

print(min(max(i, dp[sum_a - i]) for i in range(sum_a + 1)))