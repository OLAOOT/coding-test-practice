import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import defaultdict

r, c = map(int, input().split())

dist = defaultdict()
for i in range(r):
    lane = input().strip()
    cnt = 0
    for p in range(1, c - 1):
        if lane[p] == '.':
            if p == c - 4:
                break
            cnt += 1
            
        else:
            dist[int(lane[p])] = cnt

dist = list(dict(dist).items())
sorted_dist = sorted(dist, key=lambda x: x[1], reverse=True)

result = [0] * 10
rank = 1
for i, team in enumerate(sorted_dist):
    if i > 0 and sorted_dist[i - 1][1] != sorted_dist[i][1]:
        rank += 1
    result[sorted_dist[i][0]] = rank

print(*result[1:], sep='\n')