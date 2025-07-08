import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
import bisect

n, m = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

split_idx = bisect.bisect(books, 0)
minus, plus = books[:split_idx], books[split_idx:]
plus.reverse()

minus.extend([0] * (m - (len(minus) % m)))
plus.extend([0] * (m - (len(plus) % m)))
max_num = max(-minus[0], plus[0])

result = 0
for b in minus[::m]:
    result -= b * 2
for b in plus[::m]:
    result += b * 2

print(result - max_num)