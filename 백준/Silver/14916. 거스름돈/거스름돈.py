import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
count = 0

while n > 0:
    if n % 5 == 0:
        count += n // 5
        break
    
    n -= 2
    count += 1

if n < 0:
    print(-1)
else:
    print(count)