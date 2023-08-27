from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    for c in course:
        combs = defaultdict(int)
        
        for order in orders:
            for comb in combinations(order, c):
                combs[tuple(sorted(comb))] += 1

        if combs:
            max_value = max(combs.values())
            if max_value >= 2:
                for comb, value in combs.items():
                    if value == max_value:
                        answer.append(''.join(comb))
    
    answer.sort()
    
    return answer