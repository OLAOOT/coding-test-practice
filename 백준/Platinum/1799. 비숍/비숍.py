import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 대각선 방문 여부
ld = [False] * (2 * n)   # 왼쪽 위 -> 오른쪽 아래
rd = [False] * (2 * n)   # 오른쪽 위 -> 왼쪽 아래

black = []
white = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            if (i + j) % 2 == 0:
                black.append((i, j))
            else:
                white.append((i, j))

def backtracking(idx, cnt, arr):
    if idx == len(arr):
        return cnt
    x, y = arr[idx]
    res = 0
    # 비숍 놓는 경우
    if not ld[x - y + n] and not rd[x + y]:
        ld[x - y + n] = rd[x + y] = True
        res = max(res, backtracking(idx + 1, cnt + 1, arr))
        ld[x - y + n] = rd[x + y] = False
    # 비숍 안 놓는 경우
    res = max(res, backtracking(idx + 1, cnt, arr))
    return res

print(backtracking(0, 0, black) + backtracking(0, 0, white))

