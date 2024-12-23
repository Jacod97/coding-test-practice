def solution(prices):
    answer = [] # 각 가격마다 초를 담아둘 공간
    
    for i in range(len(prices)-1): # 마지막껀 무조건 0이라 계산안함
        count = 0 
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]: # 이전 가격보다 작아지면 더 카운트 할 필요가 없어 멈춤
                count += 1 # 근데 더 작아져도 도달시간까지는 측정
                break
            else: # 이전가격보다 크면 1초씩 증가
                count += 1
        answer.append(count)
    answer.append(0) # 마지막 가격은 비교할 가격이 없기때문에 무조건 0
    return answer




# from collections import deque

# def solution(prices):
#     stack = [] 
#     q = deque(prices)
    
#     while len(q) > 1: # 제일마지막껀 무조건 0이라 의미 없음
#         cp = q.popleft() # cp(current price)와 np(next prcie)를 분리
#         seconds = 0 # 가격이 떨어지지않는 기간
        
#         for np in q: 
#             seconds += 1 # 한번 비교할때마다 1초씩 증가   
#             if cp > np: # 현재가격이 크면 더 비교해볼 이유가 없음
#                 break
                
#         stack.append(seconds) # cp비교를 할때마다 seconds를 스택에 저장
#     stack.append(0) # 마지막은 무조건 0초
#     return stack