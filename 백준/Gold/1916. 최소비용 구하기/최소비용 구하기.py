import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)
n = int(input())
m = int(input())
node = [[] for _ in range(n + 1)]
cost = [INF] * (n + 1)

for _ in range(m):
    s, e, c = map(int, input().split())
    node[s].append((c, e))

start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
cost[start] = 0

while q:
    now_c, now = heapq.heappop(q)
    if cost[now] < now_c:
        continue
    for new_c, new in node[now]:
        if now_c + new_c < cost[new]:
            cost[new] = now_c + new_c
            heapq.heappush(q, (cost[new], new))

print(cost[end])