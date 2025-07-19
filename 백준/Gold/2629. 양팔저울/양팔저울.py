import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
beads = list(map(int, input().split()))

MAX = 40000
dp = [[False] * (MAX + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    for j in range(MAX + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
            
            if j + weights[i] <= MAX:
                dp[i + 1][j + weights[i]] = True
                
            dp[i + 1][abs(j - weights[i])] = True

result = []
for b in beads:
    result.append('Y' if dp[n][b] else 'N')

print(' '.join(result))