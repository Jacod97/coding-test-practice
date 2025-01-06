def solution(k, tangerine):
    orange = {}
    for size in tangerine:
        if size in orange:
            orange[size] += 1
        else:
            orange[size] = 1
    orange_count = sorted(list(orange.values()))
    
    count = 0
    while k > 0:
        k -= orange_count.pop()
        count += 1
        
    return count