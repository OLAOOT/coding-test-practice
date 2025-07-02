import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
import heapq

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]
classes.sort()

q = []
heapq.heappush(q, classes[0][1])

for c in classes[1:]:
    if q[0] <= c[0]:
        heapq.heappop(q)
    heapq.heappush(q, c[1])

print(len(q))