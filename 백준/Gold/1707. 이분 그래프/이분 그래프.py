import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

def is_bipartite(v, graph):
    color = [0] * (v + 1)  # 0: 미방문, 1: a, -1: b

    for start in range(1, v + 1):
        if color[start] == 0:
            q = deque([start])
            color[start] = 1
            while q:
                cur = q.popleft()
                for nxt in graph[cur]:
                    if color[nxt] == 0:
                        color[nxt] = -color[cur]
                        q.append(nxt)
                    elif color[nxt] == color[cur]:
                        return False
    return True

t = int(input())
for _ in range(t):
    v_num, e = map(int, input().split())
    graph = [[] for _ in range(v_num + 1)]
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    print("YES" if is_bipartite(v_num, graph) else "NO")