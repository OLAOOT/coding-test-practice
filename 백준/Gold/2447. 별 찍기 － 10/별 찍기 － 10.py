import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
arr = [[' '] * n for _ in range(n)]

def dac(x, y, n):
    if n == 3:
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                arr[i][j] = '*'
        arr[x + 1][y + 1] = ' '
    else:
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    dac(x + i * n // 3, y + j * n // 3, n // 3)
dac(0, 0, n)
for r in arr:
    print(*r, sep='')