def compare(x, y):
    # 두 숫자 문자열을 이어 붙였을 때 큰 값을 기준으로 비교
    if x + y > y + x:
        return x
    else:
        return y
    
def merge_sort(arr):
    if len(arr) <= 1: # 재귀호출 하다가 요소가 1개가 되면 종료
        return arr
    
    mid = len(arr) // 2 # 반짤라서 두 그룹으로 만듬(이것이 merge_sort)
    arrA = merge_sort(arr[:mid]) # mid 를 기준으로 자른 후 정렬함
    arrB = merge_sort(arr[mid:])  

    sort_arr = [] # 정렬된 값을 담아야 함

    while arrA and arrB: # 둘중 하나라도 비어 있으면 끝
        if arrA[0] == compare(arrA[0],arrB[0]):
            sort_arr.append(arrA.pop(0))
        else:
            sort_arr.append(arrB.pop(0))
    # while 종료 후 숫자가 남아 있다면 arrA가 False가 될때까지 pop해야함
    while arrA:
        sort_arr.append(arrA.pop(0))
    while arrB:
        sort_arr.append(arrB.pop(0))
    return sort_arr

def solution(numbers):
    arr = list(map(str,numbers)) # numbers가 정수이기 때문에 문자열로 바꿔줌
    answer = merge_sort(arr) # merge_sort함

    while answer[0] == "0": #ex) 제일 앞자리가 0일 경우 "0620"이 아닌 "620"
        answer.pop(0)
        if len(answer) < 2: #ex) "000"일 경우 "0"으로 해야함
            break

    return ''.join(answer)