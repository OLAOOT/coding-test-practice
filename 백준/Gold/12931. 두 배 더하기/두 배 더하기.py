import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
b = list(map(int, input().split()))
cnt = 0

while any(x != 0 for x in b):
    for i in range(n):
        if b[i] % 2 == 1:
            b[i] -= 1
            cnt += 1

    if all(x == 0 for x in b):
        break
    else:
        b = [int(x / 2) for x in b]
        cnt += 1

print(cnt)