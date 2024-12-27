def solution(k, m, score):
    score.sort(reverse=True) # 스코어를 내림차순으로 정렬
    
    bottari = [] # 길이 m만큼 보따리에 담는다
    start=0
    end = m
    while end<=len(score):
        bottari.append(score[start:end])
        start += m
        end += m
        
    answer = 0 # 한보따리당 최솟값 곱하기 m을 해서 answer에 쌓아준다
    for i in range(len(bottari)):
        answer += bottari[i][-1] * m
    return answer