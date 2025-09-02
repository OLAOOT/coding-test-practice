import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(int, input().split()))
dice_r = deque([0, 0, 0])
dice_c = deque([0, 0, 0, 0]) # dice_r[1] == dice_c[1]
dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]

def copy(x, y):
    global graph, dice_c
    if graph[x][y] == 0:
        graph[x][y] = dice_c[3]
    else:
        dice_c[3] = graph[x][y]
        graph[x][y] = 0
        
def move(cmd):
    if cmd == 1:
        dice_r.rotate(1)
        dice_r[0], dice_c[3] = dice_c[3], dice_r[0]
        dice_c[1] = dice_r[1]
    elif cmd == 2:
        dice_r.rotate(-1)
        dice_r[2], dice_c[3] = dice_c[3], dice_r[2]
        dice_c[1] = dice_r[1]
    elif cmd == 3:
        dice_c.rotate(-1)
        dice_r[1] = dice_c[1]
    else:
        dice_c.rotate(1)
        dice_r[1] = dice_c[1]

for cmd in cmds:
    if 0 <= x + dx[cmd] < n and 0 <= y + dy[cmd] < m:
        x += dx[cmd]
        y += dy[cmd]
        move(cmd)
        copy(x, y)
        print(dice_r[1])