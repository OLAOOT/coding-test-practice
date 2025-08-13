import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

cycle = []

def find_cycle(x, visited):
    global nums
    global cycle
    
    if nums[x] in cycle:
        return
    
    for i, v in enumerate(visited):
        if v == nums[x]:
            cycle += visited[i:]
            return

    find_cycle(nums[x], visited + [nums[x]])

n = int(input())
nums = [0] + [int(input()) for _ in range(n)]

for i in range(1, n + 1):
    find_cycle(i, [i])

print(len(cycle))
cycle.sort()
for c in cycle:
    print(c)