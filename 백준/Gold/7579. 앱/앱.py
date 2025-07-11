import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n, req_m = map(int, input().split())

ms = [0] + list(map(int, input().split()))
cs = [0] + list(map(int, input().split()))
dp = [[0] * (sum(cs) + 1) for _ in range(n + 1)]
result = int(1e9)

# i: 메모리, j: 코스트 (테이블: 해당 코스트를 이용해 최대로 얻을 수 있는 메모리)
for i in range(1, n + 1):
    for j in range(sum(cs) + 1):
        if j < cs[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - cs[i]] + ms[i], dp[i - 1][j])
        if dp[i][j] >= req_m:
            result = min(result, j)
print(result)