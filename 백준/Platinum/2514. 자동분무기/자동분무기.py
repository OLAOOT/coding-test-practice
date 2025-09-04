'''
d5에 배치된 기계 = Xd5 <<< -1 or 1 or 0, 구하고자 하는 값
d5의 생산량 = Od5 <<< input으로 받는 값

Od5 = Xd + X5 - Xd5 <<< 까지는 자명함
Od = (Xd + X1 - Xd1) + ... + (Xd + X8 - Xd8) = 8Xd + XAll - Xd = XAll + 7Xd
OAll = 8XAll + 7(Xa + ... + Xh) = 8XAll + 7XAll = 15XAll <<< 배치된 기계의 총합 = 생산량 총합 / 15, XAll의 값 구할 수 있음

O5 = (Xa + X5 - Xa5) + ... + (Xh + X5 - Xh5) = 8X5 + XAll - X5 = XAll + 7X5
Od + O5 = 2XAll + 7(Xd + X5) = 2XAll + 7(Od5 + Xd5) <<< 맨 위의 식으로 치환
따라서 Xd5 = (Od + O5 - 2XAll) / 7 - Od5
'''

import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

default = int(input())
n = int(input())
graph = [[x - default for x in list(map(int, input().split()))] for _ in range(8)]
o_all = sum([sum(r) for r in graph])
x_all = o_all // 15

x = [['.'] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        machine = (sum(graph[i]) + sum([r[j] for r in graph]) - 2 * x_all) // 7 - graph[i][j]
        if machine == 1:
            x[i][j] = '+'
        elif machine == -1:
            x[i][j] = '-'

for r in x:
    print(' '.join(r))