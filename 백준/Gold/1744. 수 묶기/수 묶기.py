import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
import bisect

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
result = 0

minus_idx = bisect.bisect(nums, -1)
zero_idx = bisect.bisect(nums, 0)
one_idx = bisect.bisect(nums, 1)
minus, zero, one, plus = nums[:minus_idx], nums[minus_idx:zero_idx], nums[zero_idx:one_idx], nums[one_idx:]
plus.reverse()

if len(minus) % 2 == 1:
    if zero:
        minus.append(0)
    else:
        result += minus[-1]

if len(plus) % 2 == 1:
    result += plus[-1]

result += len(one)

for ns in minus, plus:
    for a, b in zip(ns[::2], ns[1::2]):
        result += a * b

print(result)