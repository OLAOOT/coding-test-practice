import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
from collections import deque

w = deque(input().strip())
s = deque(input().strip())
q_f, q_b = deque(), deque()
w_len = len(w)

'''
s를 stack. s가 없으면 반대쪽 q까지 끌어와 스택
그 도중 검열시 반대 차례로 넘김을 반복
반대쪽 q마저 없으면 현재의 q를 프린트하고 종료
'''

def censor_f():
    global q_f
    if len(q_f) < w_len:
        return False
        
    temp_q = deque()
    
    for _ in range(w_len):
        temp_q.appendleft(q_f.pop()) # 슬라이싱보다 이게 빠름
        
    if temp_q == w:
        return True
    else:
        for _ in range(w_len):
            q_f.append(temp_q.popleft()) # 덧셈으로 concat보다 이게 빠름
        return False
        
def censor_b():
    global q_b
    if len(q_b) < w_len:
        return False
        
    temp_q = deque()
    
    for _ in range(w_len):
        temp_q.append(q_b.popleft())
        
    if temp_q == w:
        return True
    else:
        for _ in range(w_len):
            q_b.appendleft(temp_q.pop())
        return False

while True:
    while True:
        if s:
            q_f.append(s.popleft())
            if censor_f():
                break
                
        elif q_b:
            q_f.append(q_b.popleft())
            if censor_f():
                break
        else:
            print(''.join(list(q_f)))
            sys.exit()

    while True:
        if s:
            q_b.appendleft(s.pop())
            if censor_b():
                break
        elif q_f:
            q_b.appendleft(q_f.pop())
            if censor_b():
                break
        else:
            print(''.join(list(q_b)))
            sys.exit()