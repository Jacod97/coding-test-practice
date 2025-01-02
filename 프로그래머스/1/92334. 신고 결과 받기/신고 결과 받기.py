def solution(id_list, report, k):
    # 공백을 기준으로 신고한놈과 당한놈으로 분류
    # 한사람이 다른 한사람을 여러번 신고할 수 없어서 set 사용
    do = [i.split() for i in set(report)]  
    # warn_list에 일단 key값만 설정
    warn_list = {i : [] for i in id_list}
    black_list = {i : 0 for i in id_list}

    for key, value in do:
        warn_list[key].append(value)
        black_list[value] += 1
    
    for key in black_list:
        if black_list[key] >= k:
            black_list[key] = 1
        else:
            black_list[key] = 0
    

    answer = {
        key : sum([black_list[i] for i in val])
        for key, val in warn_list.items()
    }
    return list(answer.values())