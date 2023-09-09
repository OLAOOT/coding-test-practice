import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
import heapq

def dijkstra(graph, n, start):
    q = []
    dist_table = [int(1e9)] * (n + 1)
    dist_table[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if dist_table[now] < dist:
            continue
        for cost, nxt in graph[now]:
            nxt_cost = dist + cost
            if nxt_cost < dist_table[nxt]:
                dist_table[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))
    return dist_table

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, time = map(int, input().split())
        graph[b].append((time, a))
    
    dist_table = dijkstra(graph, n, c)
    dist_table = [dist for dist in dist_table if dist != int(1e9)]
    print(len(dist_table), max(dist_table))