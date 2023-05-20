import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

def product(a, b):
    return a[0] * b[1] - a[1] * b[0]

p = [tuple(map(int, input().split())) for _ in range(3)]

a = (p[0][0] - p[1][0], p[0][1] - p[1][1])
b = (p[2][0] - p[1][0], p[2][1] - p[1][1])

result = product(a, b)
if result > 0:
    print(-1)
elif result < 0:
    print(1)
else:
    print(0)