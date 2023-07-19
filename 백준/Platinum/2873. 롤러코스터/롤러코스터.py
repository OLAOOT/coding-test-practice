import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = ''

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def ride(r, c, even=False):
    global answer
    
    if c % 2 == 1:
        for _ in range(c // 2):
            answer += 'D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R'
        if not even:
            answer += 'D' * (r - 1)
                
    else: # r % 2 == 1 or 짝수
        for _ in range(r // 2):
            answer += 'R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D'
        if not even:
            answer += 'R' * (c - 1)

if n % 2 == 1 or m % 2 == 1:
    ride(n, m)
elif n == m == 2:
    if graph[0][1] > graph[1][0]:
        answer += 'RD'
    else:
        answer += 'DR'
    
else:
    rx, ry = 0, 1
    # 뺄 부분 하나 찾기
    for i in range(n):
        if i % 2 == 0:
            for j in range(1, m, 2):
                if graph[i][j] < graph[rx][ry]:
                    rx, ry = i, j
        else:
            for j in range(0, m, 2):
                if graph[i][j] < graph[rx][ry]:
                    rx, ry = i, j
    
    zx = rx if rx % 2 == 0 else rx - 1
    # 뺄 부분까지 이동
    ride(zx, m, True)
    # 뺄 부분 피해서 지그재그
    if ry == 0:
        answer += 'R' + 'DRUR' * (m // 2 - 1) + 'D'
    elif ry == m - 1:
        answer += 'DRUR' * (m // 2 - 1) + 'DR'
    else:
        y = 0
        while y != m - 1:
            if y == ry:
                answer += 'R'
                y += 1
                if y == m - 1:
                    break
            answer += 'DR'
            y += 1
            if y == ry:
                answer += 'R'
                y += 1
            answer += 'UR'
            y += 1
        answer += 'D'
    # 지그재그 이후
    if zx != n - 2:
        answer += 'D' + 'L' * (m - 1) + 'D'
        ride(n - rx - 3, m)
    
print(answer)