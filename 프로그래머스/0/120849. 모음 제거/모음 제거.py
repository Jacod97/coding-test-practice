def solution(my_string):
    moum = [i for i in "aeiou"]
    answer = [i for i in my_string if i not in moum]
    return ''.join(answer)