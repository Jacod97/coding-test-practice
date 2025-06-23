def solution(n):
    text = str(n)
    answer = 0
    for i in text:
        answer += int(i)
    return answer