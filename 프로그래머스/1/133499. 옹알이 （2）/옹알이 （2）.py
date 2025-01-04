def mussg(babbling, accent):
    result = []
    for baby in babbling:
        if accent+accent in baby:
            continue
        temp = baby.replace(accent,'0')
        result.append(temp)
    return result

def solution(babbling):
    joka = ["aya", "ye", "woo", "ma"]
    
    for umm in joka:
        babbling = mussg(babbling, umm)
    answer = []
    for i in babbling:
        a = i.replace('0', '')
        answer.append(a)
    return answer.count('')