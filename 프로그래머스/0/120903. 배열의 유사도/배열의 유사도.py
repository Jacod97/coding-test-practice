def solution(s1, s2):
    answer = [i for i in s2 if i in s1]
    return len(answer)