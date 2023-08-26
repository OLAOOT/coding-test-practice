from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_diff = -1
    
    for combination in combinations_with_replacement(range(11), n):
        scores = [0] * 11
        for score in combination:
            scores[10 - score] += 1
            
        ryan, apeach = 0, 0
        for idx in range(10):
            if scores[idx] > info[idx]:
                ryan += 10 - idx
            elif info[idx] != 0:
                apeach += 10 - idx
                
        if ryan > apeach and ryan - apeach > max_diff:
            answer = scores
            max_diff = ryan - apeach
            
    return answer