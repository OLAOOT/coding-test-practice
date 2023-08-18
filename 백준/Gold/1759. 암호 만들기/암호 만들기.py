import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

from itertools import combinations

l, c = map(int, input().split())
letter = input().strip().split()

answer = []
for word in combinations(letter, l):
    v_count = 0
    for vowel in ('a', 'e', 'i', 'o', 'u'):
        if vowel in word:
            v_count += 1
    if v_count == 0 or l - v_count < 2:
        continue    
    answer.append(''.join(sorted(word)))

for i in sorted(answer):
    print(i)