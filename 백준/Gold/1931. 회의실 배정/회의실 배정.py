import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda m: (m[1], m[0]))

cnt = 1
end_time = meetings[0][1]

for m in meetings[1:]:
    if end_time <= m[0]:
        cnt += 1
        end_time = m[1]

print(cnt)