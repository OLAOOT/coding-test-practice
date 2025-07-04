import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
k = int(input())
points = list(map(int, input().split()))
points.sort()

if n == 1:
    print(0)
elif k == 1:
    print(points[-1] - points[0])
else:
    dists = [points[i + 1] - points[i] for i in range(len(points) - 1)]
    dists.sort()
    print(sum(dists[:-(k - 1)]))