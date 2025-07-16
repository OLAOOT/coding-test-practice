import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

c, n = map(int, input().split())

cities = [list(map(int, input().split()))for _ in range(n)]
dp = [0]

while dp[-1] < c:
    v = 0
    length = len(dp)
    for city in cities:
        if city[0] > length:
            continue
        v = max(v, dp[length - city[0]] + city[1])
    dp.append(v)
    
print(len(dp) - 1)