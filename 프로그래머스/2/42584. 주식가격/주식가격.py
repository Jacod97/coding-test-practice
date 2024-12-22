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