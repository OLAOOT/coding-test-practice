import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

gears = [deque(list(input().strip())) for _ in range(4)]

k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    n -= 1
    turn = [n]
    
    order = [(1, 2, 3), (0, 2, 3), (1, 0, 3), (2, 1, 0)]
    
    if n == 0:
        for i in (1, 2, 3):
            if gears[i - 1][2] != gears[i][6]:
                turn.append(i)
            else:
                break
    elif n == 1:
        if gears[1][6] != gears[0][2]:
            turn.append(0)
        for i in (2, 3):
            if gears[i - 1][2] != gears[i][6]:
                turn.append(i)
            else:
                break
    elif n == 2:
        for i in (1, 0):
            if gears[i + 1][6] != gears[i][2]:
                turn.append(i)
            else:
                break
        if gears[2][2] != gears[3][6]:
            turn.append(3)
    else:
        for i in (2, 1, 0):
            if gears[i + 1][6] != gears[i][2]:
                turn.append(i)
            else:
                break
    
    for i in turn:
        if abs(i - n) % 2 == 0:
            gears[i].rotate(d)
        else:
            gears[i].rotate(-d)

answer = 0
for i in range(4):
    answer += int(gears[i][0]) * (2 ** i)
print(answer)