import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
dx = [-1, 0, 1]
goal = c - 1
cnt = 0

def dfs(x, y):
    if y == goal:
        return True

    for d in range(3):
        nx, ny = x + dx[d], y + 1
        if 0 <= nx < r and graph[nx][ny] == '.':
            graph[nx][ny] = 'x'
            if dfs(nx, ny):
                return True
    return False

for i in range(r):
    if dfs(i, 0):
        cnt += 1

print(cnt)