import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())

i = 1

while n >= i:
    n -= i
    i += 1
print(i - 1)