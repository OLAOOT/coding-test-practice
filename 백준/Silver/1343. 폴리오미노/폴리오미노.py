import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

b = input()

b = b.replace("XXXX", "AAAA")
b = b.replace("XX", "BB")

print(-1) if 'X' in b else print(b)