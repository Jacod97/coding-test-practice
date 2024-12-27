def solution(cards1, cards2, goal):
    go = [i for i in goal if i in cards1]
    al = [i for i in goal if i in cards2] 
    
    count = 0
    for i in range(len(go)):
        if go[i] != cards1[i]:
            return "No"
        else:
            count += 1
    
    for j in range(len(al)):
        if al[j] != cards2[j]:
            return "No"
        else:
            count += 1
    if count == len(goal):
        return "Yes"
        