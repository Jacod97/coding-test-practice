from collections import deque

def solution(prices):
    stack = []
    q = deque(prices)
    
    while len(q) > 1:
        cp = q.popleft()
        seconds = 0
        
        for np in q:
            seconds += 1   
            if cp > np:
                break
                
        stack.append(seconds)
    stack.append(0)
    return stack
