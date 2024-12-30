def solution(clothes):
    # a : 3 , b : 2 , c : 3 씩 있다면 
    # (3 + 2 + 3) + (3*2) + (3*3) + (2*3) + (3*2*3) 이 정답일듯?
    
    # step1. 종류별 갯수 저장
    kind = {i[1]:0 for i in clothes}
    for x,y in clothes:
        kind[y] += 1
        
    # step2 갯수만 추출
    nums = list(kind.values())
    
    # step3 (x+a)(x+b)(x+c)....와 같은 방정식 구조가 나오네요?
    # 다차방정식의 계수의 합을 구하면 정답일듯?  # 1을빼야 정답인데 이유는 모르겠음
    answer = 1
    for i in nums:
        answer *= (i+1)
    return answer-1
