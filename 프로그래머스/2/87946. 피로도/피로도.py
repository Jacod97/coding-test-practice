def solution(k, dungeons):
    max_count = 0 
    
    def dfs(pirodo, count, new_dungeons):
        nonlocal max_count
        max_count = max(max_count, count) 
        
        for i, (need, consume) in enumerate(new_dungeons):
            if pirodo >= need:  
                dfs(pirodo - consume, count + 1, new_dungeons[:i] + new_dungeons[i+1:])
    
    dfs(k, 0, dungeons) 
    return max_count
