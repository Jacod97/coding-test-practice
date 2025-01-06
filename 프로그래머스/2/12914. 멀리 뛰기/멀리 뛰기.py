import math
def solution(n): 
    answer = 0
    start = n//2
    k = start
    
    if n%2==1 :
        start += 1
    
    for i in range(start, n+1): 
        answer += math.comb(i,k)
        k -= 1
        
    return answer % 1234567