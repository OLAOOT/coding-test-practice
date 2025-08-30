import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())

def add(a, b): # [1, 2, 3] + [4, 5, 6] = [5, 7, 9]
    return [x + y for x, y in zip(a, b)]
    
def split_num(n): # 123 = [100, 20, 3]
    digits = list(str(n))
    length = len(digits)
    result = []

    for i, d in enumerate(digits):
        place = 10 ** (length - i - 1)
        result.append(int(d) * place)

    return result

def calc(n): # n이 4000이라면, 4000~4999를 계산 / n이 800000이라면, 800000~899999를 계산. 10부터 가능
    digit = len(str(n)) - 1 # 자리수 예: 1234면 3
    first_n = int(str(n)[0]) # 맨 앞자리 숫자
    result = [10 ** (digit - 1) * digit] * 10 # n이 1000의 자리라면, 100의자리 100번, 10의자리 100번, 1의자리 100번씩 나옴
    result[first_n] += 10 ** digit # n이 1000의 자리라면, 맨 앞 숫자만 1000번 더 나옴
    return result

def skip_calc(n): # n이 100000이라면, 1~99999를 계산. 10부터 가능
    cur = 10
    digit = 1 # 자리수
    
    # 1 ~ 9
    result = [0] + [1] * 9
    
    while cur != n:
        tmp1 = [10 ** (digit - 1) * digit * 9] * 10 # n이 1000의 자리라면, 100의자리 100번, 10의자리 100번, 1의자리 100번씩, 9번 나옴
        tmp2 = [0] + [10 ** (digit)] * 9 # n이 1000의 자리라면, 0 빼고 다 1000번씩 더 나옴
        result = add(result, tmp1)
        result = add(result, tmp2)
        cur *= 10
        digit += 1
    
    return result

result = [0] * 10
# 0. 1의 자리 수일 경우
if n < 10:
    for i in range(1, n + 1):
        result[i] += 1
    print(' '.join(map(str, result)))
else:
    # 예) 345678
    # 1. 1~99999
    splited = split_num(n) # [300000, 40000, 5000, 600, 70, 8]
    place = 10 ** (len(str(n)) - 1) # 100000
    result = add(result, skip_calc(place))
    
    # 2. 100000~299999
    for i in range(place, splited[0], place):
        result = add(result, calc(i))
    
    # 3. 300000~339999 ~ 345660~345669
    # "00000~09999" + 10000~19999 + 20000~29999 + 30000~39999 + 3이 40000번
    # 00000~09999 계산: 만의자리에 0이 10000번 나옴. 나머지는 4000번씩(1000 + 1000 + 1000 + 1000) 나옴 (즉 0은 14000번, 나머지 4000번)
    for idx in range(1, len(splited) - 1):
        num = splited[idx]
        digit = len(str(num)) - 1 # 자리수. 40000이면 4
        if digit == 0:
            continue
        place = 10 ** digit # 40000이면 10000
        result = add(result, [10 ** (digit - 1) * digit] * 10) # 00000~09999 계산 중, 전부 4000번 더함
        result = add(result, [place] + [0] * 9) # 00000~09999 계산 중, 0에만 10000번 더함
        
        for i in range(place, num, place):
            result = add(result, calc(i)) # 10000~39999
        for prev_num in splited[:idx]:
            result[int(str(prev_num)[0])] += num # 앞 자리들을 현재 num만큼
    
    # 4. 345670~345678
    final_num = splited[-1]
    for i in range(final_num + 1):
        result[i] += 1
    for prev_num in splited[:-1]:
        result[int(str(prev_num)[0])] += final_num + 1 # 앞 자리들을 final_num만큼
    
    print(' '.join(map(str, result)))