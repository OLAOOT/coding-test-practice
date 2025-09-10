import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

# 에라토스테네스의 체
def sieve(n):
    MAX = n + 1
    LIM = int(n ** 0.5) + 1 # 제곱근 까지만 계산해도 됨
    SET = lambda start, end, gap: set(range(start, end, gap))

    '''5 (mod 6)들과 1 (mod 6)들을 참으로 설정
        모든 정수는 6으로 나누면 다음 중 하나:
        0 mod 6 → 6, 12, 18, … (전부 2와 3의 배수 → 소수 ❌)
        1 mod 6 → 1, 7, 13, 19, … (소수 가능성 있음 ✅)
        2 mod 6 → 2, 8, 14, … (2의 배수 → 소수 ❌ 단, 2는 예외)
        3 mod 6 → 3, 9, 15, … (3의 배수 → 소수 ❌ 단, 3은 예외)
        4 mod 6 → 4, 10, 16, … (2의 배수 → 소수 ❌)
        5 mod 6 → 5, 11, 17, 23, … (소수 가능성 있음 ✅)
        즉 2, 3을 제외한 모든 소수는 5 mod 6이거나 1 mod 6임. 2의 배수와 3의 배수 계산 안해도 돼서 빠르게 계산 가능
        단, 1은 소수가 아니기에 1 (mod 6)은 7부터 시작'''

    prime = SET(5, MAX, 6)| SET(7, MAX, 6)
    if n > 2: prime.add(3) # 예외처리
    if n > 1: prime.add(2) # 예외처리

    for i in range(5, LIM, 6):
        # 5 (mod 6) 부분 (5, 11, 17, 23, ...에 관해 반복)
        # i는 5 mod 6의 소수 후보이고, i * i부터 시작해서 "i * 6 간격"으로 배수를 제거
        # 동시에 i * (i + 2), 즉 1 mod 6 계열 배수도 제거 (일종의 최적화)
        if i in prime:
            prime -= SET(i * i, MAX, i * 6) | SET(i * (i + 2), MAX, i * 6)

        # 1 (mod 6) 부분 (위와 동일한 방식)
        j = i + 2
        if j in prime:
            prime -= SET(j * j, MAX, j * 6) | SET(j * (j + 4), MAX, j * 6)

    return sorted(list(prime))



n = int(input())
# 1 ~ 4의 수 입력받을시 처리
exception = [0, 0, 1, 1, 0]
if n < 5:
    print(exception[n])
    sys.exit()

cnt = 0
prime = sieve(n)
# print(prime)
prime_len = len(prime)
l, r = 0, 1 # pointer
s = 5

while l <= r:
    # print(l, r)
    if s == n:
        cnt += 1
    if s < n:
        r += 1
        if r == prime_len:
            break
        s += prime[r]
    else:
        s -= prime[l]
        l += 1
print(cnt)