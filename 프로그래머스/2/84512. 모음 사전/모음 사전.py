def solution(word):
    count = 0
    flag = False
    moum = ["A","E","I","O","U"]

    def dfs(result,depth):
        nonlocal count, flag
        if ''.join(result) == word:
            flag = True
            return
        if depth == 5:
            return 
        
        for s in moum:
            result.append(s)
            count += 1
            dfs(result,depth+1)
            if flag:
                return
            result.pop()
            
    dfs([],0)
    return count