import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

def bfs(hx, hy, cs, px, py):
    q = deque([(hx, hy)])
    
    while q:
        x, y = q.popleft()
        if abs(x - px) + abs(y - py) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = cs[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = True
    print("sad")
    return

t = int(input())
for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    cs = [list(map(int, input().split())) for _ in range(n)]
    px, py = map(int, input().split())
    
    visited = [False for _ in range(n + 1)] 
    bfs(hx, hy, cs, px, py)