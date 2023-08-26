import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

inf = 1e6

n = int(input())
graph = list(map(int, input().split()))
max_dp, min_dp = graph[:], graph[:]
max_tmp, min_tmp = [0] * 3, [0] * 3

for i in range(n - 1):
    graph = list(map(int, input().split()))
    max_tmp[0] = graph[0] + max(max_dp[0], max_dp[1])
    max_tmp[1] = graph[1] + max(max_dp[0], max_dp[1], max_dp[2])
    max_tmp[2] = graph[2] + max(max_dp[1], max_dp[2])
    min_tmp[0] = graph[0] + min(min_dp[0], min_dp[1])
    min_tmp[1] = graph[1] + min(min_dp[0], min_dp[1], min_dp[2])
    min_tmp[2] = graph[2] + min(min_dp[1], min_dp[2])
    max_dp = max_tmp[:]
    min_dp = min_tmp[:]
    
print(max(max_dp), min(min_dp))