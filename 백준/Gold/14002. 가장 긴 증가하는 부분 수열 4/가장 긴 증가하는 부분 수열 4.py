import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
series = list(map(int, input().split()))
dp = [1] * n
dp_s = [[s] for s in series]

for i in range(n):
    for j in range(i):
        if (series[i] > series[j] and dp[j] + 1 > dp[i]):
            dp[i] = dp[j] + 1
            dp_s[i] = [s for s in dp_s[j]] + [series[i]]

max_len = max(dp)
print(max_len)
print(' '.join(map(str, dp_s[dp.index(max_len)])))