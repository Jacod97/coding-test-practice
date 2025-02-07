def solution(s):
    answer = []
    n = 0
    for i in s:
        if n == 0 or n % 2 == 0:
            answer.append(i.upper())
        else:
            answer.append(i.lower())
        n += 1
        if i == ' ':
            n = 0
    return ''.join(answer)