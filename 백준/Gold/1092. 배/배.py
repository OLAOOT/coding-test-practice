import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
cargos = list(map(int, input().split()))

cranes.sort(reverse=True)
cargos.sort(reverse=True)
cnt = 0

if cranes[0] < cargos[0]:
    print(-1)
else:
    while cargos:
        for crane in cranes:
            if cargos and crane < cargos[-1]:
                continue
            for cargo in cargos:
                if crane >= cargo:
                    cargos.remove(cargo)
                    break
                    
        cnt += 1
    print(cnt)