import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

n, k = map(int, input().split())
belt = deque([None]) + deque(list(map(int, input().split())))
robots = deque([])
cnt = 0
while belt.count(0) < k:
    cnt += 1
    rotated_belt = deque(list(belt)[1:])
    rotated_belt.rotate(1)
    belt = deque([None]) + rotated_belt
    if robots:
        robots = deque([x + 1 for x in robots])
        if robots[0] == n:
            robots.popleft()
        
    if robots:
        if belt[robots[0] + 1] != 0:
            robots[0] += 1
            belt[robots[0]] -= 1
        for i in range(1, len(robots)):
            if robots[i - 1] != robots[i] + 1 and belt[robots[i] + 1] != 0:
                robots[i] += 1
                belt[robots[i]] -= 1
        
        if robots[0] == n:
            robots.popleft()
        
    if belt[1] != 0:
        robots.append(1)
        belt[1] -= 1

print(cnt)