def solution(arr):
    count = 0
    for i in arr:
        count += i
    return count / len(arr)