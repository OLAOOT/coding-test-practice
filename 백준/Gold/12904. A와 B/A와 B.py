import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

s1 = list(input().strip())
s2 = list(input().strip())

while len(s1) < len(s2):
    if s2.pop() == 'B':
        s2.reverse()

print(1) if s1 == s2 else print(0)