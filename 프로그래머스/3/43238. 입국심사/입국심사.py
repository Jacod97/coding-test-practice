def pointer(n,times,mid):
    people = 0
    for time in times:
        people += mid // time 
    
    if people >= n: #대기 인원 보다 mid시간 내에 더 많거나 같은 인원 수용가능
        return True
    else:
        return False
    
def solution(n,times):
    times.sort()
    left = 0 # 제한 사항에 1분 이상이래
    right = times[-1] * n # 최악의 대기 시간
    answer = 0 # mid 계속 담아야지

    def binary_search(left,right):
        nonlocal answer
        mid = (left+right) // 2
        if left == right: # 탈출 조건
            return 

        if pointer(n,times,mid): # n명의 인원이 수용 가능하면
            answer = mid # 정답을 mid로 일단 해놔
            binary_search(left,mid-1) # 그리고 right값 줄여봐 (left와 만나기 위해)
        else:
            binary_search(mid+1,right) # n명의 인원 수용 불가능하면 증가시켜야지
        

    binary_search(left,right)
    return answer # 응 안돼~