import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)