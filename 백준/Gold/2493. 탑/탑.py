import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
result = [0] * n

towers = list(map(int, input().split()))
stack = []

for i in range(n, 0, -1):
    tower = towers.pop()
    if not stack:
        stack.append((tower, i))
    else:
        while stack and stack[-1][0] < tower:
            result[stack.pop()[1] - 1] = i
        stack.append((tower, i))

print(*result)