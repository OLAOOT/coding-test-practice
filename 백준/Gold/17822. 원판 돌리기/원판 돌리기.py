import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

n, m, t = map(int, input().split())
discs = [deque([])] + [deque(list(map(int, input().split()))) for _ in range(n)]
last_idx = m - 1

def calc_avg(x, avg):
    if x > avg:
        return x - 1
    elif x < avg:
        return x + 1
    else:
        return x

for _ in range(t):
    x, d, k = map(int, input().split())
    d = -1 if d else 1
    # 돌리기
    for i in range(x, n + 1, x):
        discs[i].rotate(d * k)
    # 지울 거 찾기
    erase_set = set()
    for i in range(1, n):
        for j in range(last_idx):
            if not discs[i][j]:
                continue
            if discs[i][j] == discs[i][j + 1]:
                erase_set.update(((i, j), (i, j + 1)))
            if discs[i][j] == discs[i + 1][j]:
                erase_set.update(((i, j), (i + 1, j)))
        if not discs[i][last_idx]:
            continue
        if discs[i][last_idx] == discs[i][0]:
            erase_set.update(((i, last_idx), (i, 0)))
        if discs[i][last_idx] == discs[i + 1][m - 1]:
            erase_set.update(((i, last_idx), (i + 1, last_idx)))
            
    for j in range(last_idx):
        if not discs[n][j]:
            continue
        if discs[n][j] == discs[n][j + 1]:
            erase_set.update(((n, j), (n, j + 1)))
    if discs[n][last_idx] and discs[n][last_idx] == discs[n][0]:
        erase_set.update(((n, last_idx), (n, 0)))

    if erase_set:
        # 지우기
        for i, j in erase_set:
            discs[i][j] = None
    else:
        cnt = sum(1 for row in discs for x in row if x is not None)
        if cnt:
            avg = sum(x for row in discs for x in row if x is not None) / cnt
            discs = [deque([calc_avg(x, avg) if x is not None else None for x in row]) for row in discs]
print(sum(x for row in discs for x in row if x is not None))