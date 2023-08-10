from itertools import combinations
import sys

tmp = list(map(int, sys.stdin.readline().split()))
n = tmp[0]
m = tmp[1]

city = []
for _ in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append([i + 1, j + 1])
        elif city[i][j] == 2:
            chickens.append([i + 1, j + 1])

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

comb = list(combinations(chickens, m))

city_chic_dist = []
for choice in comb:
    result = 0
    for house in houses:
        chic_dist = []
        for chicken in choice:
            chic_dist.append(dist(house, chicken))
        result += min(chic_dist)
    city_chic_dist.append(result)

print(min(city_chic_dist))