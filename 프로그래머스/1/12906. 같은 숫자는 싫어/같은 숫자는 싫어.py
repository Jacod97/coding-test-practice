def solution(arr):
    stack = []
    stack.append(arr.pop(0)) # 첫번째 항 스택에 넣기
    
    for i in arr:
        if stack[-1] == i:
            pass
        else:
            stack.append(i)
            
    return stack