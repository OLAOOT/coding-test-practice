import math

def d_to_k(n, k):
    result = ''
    while n > 0:
        result = str(n % k) + result
        n //= k
    return result

def check_prime(n):
    if n == 1:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    n = d_to_k(n, k)
    p_list = n.split('0')
    
    for p in p_list:
        if p and check_prime(int(p)):
            answer += 1
    
    return answer