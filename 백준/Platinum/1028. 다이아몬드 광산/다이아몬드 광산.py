import sys

r, c = map(int, sys.stdin.readline().split())

graph = []
for _ in range(r):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

ul = [g[:] for g in graph]
ur = [g[:] for g in graph]
dl = [g[:] for g in graph]
dr = [g[:] for g in graph]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 1:
            if i >= 1 and j >= 1:
                ul[i][j] += ul[i - 1][j - 1]
            if i >= 1 and j < c - 1:
                ur[i][j] += ur[i - 1][j + 1]
for i in range(r - 1, -1, -1):
    for j in range(c):
        if graph[i][j] == 1:
            if i < r - 1 and j >= 1:
                dl[i][j] += dl[i + 1][j - 1]
            if i < r - 1 and j < c - 1:
                dr[i][j] += dr[i + 1][j + 1]

answer = 0
for i in range(r):
    for j in range(c):
        max_size_u = min(dl[i][j], dr[i][j])
        max_size_l = min(ur[i][j], dr[i][j])
        if max_size_u > answer:
            for size in range(max_size_u, answer, -1):
                if dr[i + size - 1][j - size + 1] >= size and \
                dl[i + size - 1][j + size - 1] >= size:
                    answer = size
        if max_size_l > answer:
            for size in range(max_size_l, answer, -1):
                if ur[i + size - 1][j + size - 1] >= size and \
                dr[i - size + 1][j + size - 1] >= size:
                    answer = size

print(answer)