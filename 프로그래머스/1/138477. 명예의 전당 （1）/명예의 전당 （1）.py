import itertools

def solution(k, score):
    stack = []   
    answer = []
    for i in range(len(score)):
        if i >= k:
            new_score = sorted(score[0:i+1], reverse=True)
            stack.append(new_score[0:k])
        else:
            stack.append(score[0:i+1])
        answer.append(min(stack[i]))
    return answer