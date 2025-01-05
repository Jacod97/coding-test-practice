def solution(N, stages):
    n = len(stages)
    stage_count = {i : stages.count(i) for i in range(1,N+2)}
    
    for key, val in stage_count.items():
        if val != 0:
            stage_count[key] = val/n
        n -= val
    count = list(stage_count.items())
    count.sort(key = lambda x:x[1], reverse = True)
    
    answer = []
    for i in range(len(count)):
        if count[i][0] > N:
            continue
        else:
            answer.append(count[i][0])
    return answer