# stack을 만들고 x,y의 최소 공배수를 저장
# arr.popleft() x,y제거
# 이제부터 시작 
# arr[0]과 stack[-1]의 최소공배수를 stack에 하나씩 쌓자
# 최종 stack이 정답

def divisor(x,y):
    div = set([i for i in range(1,x+1) if x % i ==0]) & set([i for i in range(1,y+1) if y % i ==0])
    return max(div)
    
def solution(arr):
    stack = []
    stack.append(arr[0]*arr[1]//divisor(arr.pop(0),arr.pop(0)))
    
    while arr:
        val1 = stack[-1]
        val2 = arr[0]
        stack.append(val1*val2//divisor(val1,val2))
        arr.pop(0)
    return stack[-1]