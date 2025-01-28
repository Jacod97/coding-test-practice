def solution(numbers, target):
    count = 0
    
    def dfs(depth,total):
        nonlocal count
        if depth == len(numbers):
            if total == target:
                count += 1
            return 
        
        plus =total + numbers[depth]
        minus = total - numbers[depth]
        dfs(depth + 1,plus)
        dfs(depth + 1,minus)
    
    dfs(0,0)
    return count