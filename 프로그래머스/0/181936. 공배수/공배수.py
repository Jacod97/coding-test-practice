def solution(number, n, m):
    result = 0
    if number % n == 0 and number % m == 0:
        result += 1
    return result