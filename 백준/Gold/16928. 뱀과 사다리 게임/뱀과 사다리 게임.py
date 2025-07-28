import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n, m = map(int, input().split())
snl_starts = []
snl_ends = []
for _ in range(n + m):
    start, end = map(int, input().split())
    snl_starts.append(start)
    snl_ends.append(end)
    
graph = [False] * 101
graph[1] = True
q = [1]
trial = 0

while True:
    trial += 1
    next_q = []
    for loc in q:
        for dice in range(1, 7):
            n_loc = loc + dice
            if n_loc <= 100 and not graph[n_loc]:
                graph[n_loc] = True
                if n_loc in snl_starts:
                    n_loc = snl_ends[snl_starts.index(n_loc)]
                    graph[n_loc] = True
                next_q.append(n_loc)
    
    if 100 in next_q:
        print(trial)
        break
    q = [v for v in next_q]