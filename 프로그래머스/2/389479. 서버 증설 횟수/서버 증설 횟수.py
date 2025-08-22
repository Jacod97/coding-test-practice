def solution(players, m, k):
    tiem_manage = [0] * (24+k)
    current = 0        
    count = 0

    for t,user in enumerate(players):
        current -= tiem_manage[t]

        need = (user) // m

        if current < need:
            add = need - current
            count += add
            current += add
            tiem_manage[t + k] += add

    return count

#이벤트 시작: 증설된 서버 수 * m < 사람 수
#이벤트 종료: k시간 후에 = 이벤트 시작 시간 + k
## 증설된 서버 수 = 현재 서버 수 + 추가 서버 수
## 증설 횟수 = 추가 서버 수
