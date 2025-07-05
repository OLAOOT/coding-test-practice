import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n, k = map(int, input().split())
talls = list(map(int, input().split()))

if n == 1:
    print(0)
elif k == 1:
    print(talls[-1] - talls[0])
else:
    diffs = [talls[i + 1] - talls[i] for i in range(len(talls) - 1)]
    diffs.sort()
    print(sum(diffs[:-(k - 1)]))