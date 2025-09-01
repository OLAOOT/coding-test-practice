import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]
targets = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            targets.append((i, j))

if not targets:
    for x in range(9):
        print(' '.join(str(sudoku[x][y]) for y in range(9)))
    sys.exit()

def backtracking(cur_idx):
    i, j = targets[cur_idx]
    
    row = sudoku[i]
    for x in range(9):
        if j == x:
            continue
        if row[j] == row[x]:
            return

    col = [row[j] for row in sudoku]
    for x in range(9):
        if i == x:
            continue
        if col[i] == col[x]:
            return
            
    sx, sy = (i // 3) * 3, (j // 3) * 3
    for x in range(3):
        for y in range(3):
            dx, dy = sx + x, sy + y
            if i == dx and j == dy:
                continue
            if sudoku[i][j] == sudoku[dx][dy]:
                return

    nxt_idx = cur_idx + 1
    
    if nxt_idx == len(targets):
        for x in range(9):
            print(' '.join(str(sudoku[x][y]) for y in range(9)))
        sys.exit()

    ni, nj = targets[nxt_idx][0], targets[nxt_idx][1]
    for x in range(1, 10):
        sudoku[ni][nj] = x
        backtracking(nxt_idx)
    sudoku[ni][nj] = 0

for x in range(1, 10):
    sudoku[targets[0][0]][targets[0][1]] = x
    backtracking(0)