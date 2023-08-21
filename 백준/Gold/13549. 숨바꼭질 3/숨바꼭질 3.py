import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

from collections import deque


def solution():
    n, k = map(int, input().split())
    t = 0
    if n >= k:
        return n - k
    
    # n < k
    graph = [1e7] * 100001
    q = deque([(n, t)])
    while q:
        now, time = q.popleft()
        
        left, right, tele, ntime = now - 1, now + 1, now * 2, time + 1
        if left >= 0 and graph[left] > ntime:
            graph[left] = ntime
            q.append((left, ntime))
        if right <= 100000 and graph[right] > ntime:
            graph[right] = ntime
            q.append((right, ntime))
        
        if tele == 0:
            continue
        if tele <= 100000 and graph[tele] > time:
            graph[tele] = time
            q.appendleft((tele, time))
    return graph[k]
print(solution())